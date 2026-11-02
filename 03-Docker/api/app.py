import json
import os

import psycopg2
import redis
from flask import Flask, jsonify, request

app = Flask(__name__)

DB = dict(
    host=os.getenv("DB_HOST", "db"),
    dbname=os.getenv("DB_NAME", "shop"),
    user=os.getenv("DB_USER", "shop"),
    password=os.getenv("DB_PASSWORD", "shop"),
    connect_timeout=3,
)
cache = redis.Redis(host=os.getenv("REDIS_HOST", "cache"), socket_connect_timeout=3)
KAFKA = os.getenv("KAFKA_BOOTSTRAP")
TOPIC = "orders.created"
_producer = None


def producer():
    global _producer
    if _producer is None:
        from kafka import KafkaProducer

        _producer = KafkaProducer(
            bootstrap_servers=KAFKA,
            value_serializer=lambda v: json.dumps(v).encode(),
            request_timeout_ms=5000,
            max_block_ms=5000,
        )
    return _producer


@app.get("/health")
def health():
    status = {}
    try:
        psycopg2.connect(**DB).close()
        status["db"] = "ok"
    except Exception as e:
        status["db"] = f"error: {e}".strip()
    try:
        cache.ping()
        status["cache"] = "ok"
    except Exception as e:
        status["cache"] = f"error: {e}"
    status["kafka"] = "disabled" if not KAFKA else "configured"
    code = 200 if all(v in ("ok", "disabled", "configured") for v in status.values()) else 503
    return jsonify(status), code


@app.get("/users")
def users():
    with psycopg2.connect(**DB) as conn, conn.cursor() as cur:
        cur.execute("SELECT id, name, email FROM users ORDER BY id")
        return jsonify([dict(id=r[0], name=r[1], email=r[2]) for r in cur.fetchall()])


@app.post("/orders")
def create_order():
    body = request.get_json(silent=True) or {}
    user_id, items = body.get("user_id"), body.get("items")
    if not user_id or not items:
        return jsonify(error="user_id and items are required"), 400

    with psycopg2.connect(**DB) as conn, conn.cursor() as cur:
        total = 0
        for it in items:
            cur.execute("SELECT price FROM products WHERE id = %s", (it["product_id"],))
            row = cur.fetchone()
            if row is None:
                return jsonify(error=f"product {it['product_id']} not found"), 404
            total += row[0] * it["qty"]
        cur.execute("INSERT INTO orders (user_id, total) VALUES (%s, %s) RETURNING id", (user_id, total))
        order_id = cur.fetchone()[0]
        for it in items:
            cur.execute(
                "INSERT INTO order_items (order_id, product_id, qty) VALUES (%s, %s, %s)",
                (order_id, it["product_id"], it["qty"]),
            )

    if KAFKA:
        try:
            producer().send(TOPIC, {"order_id": order_id, "user_id": user_id, "total": float(total)}).get(timeout=5)
        except Exception as e:
            return jsonify(order_id=order_id, warning=f"saved but event not published: {e}"), 202
    return jsonify(order_id=order_id, total=float(total)), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
