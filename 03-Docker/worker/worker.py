import json
import os

import psycopg2
from kafka import KafkaConsumer

DB = dict(
    host=os.getenv("DB_HOST", "db"),
    dbname=os.getenv("DB_NAME", "shop"),
    user=os.getenv("DB_USER", "shop"),
    password=os.getenv("DB_PASSWORD", "shop"),
)

consumer = KafkaConsumer(
    "orders.created",
    bootstrap_servers=os.environ["KAFKA_BOOTSTRAP"],
    group_id=os.getenv("KAFKA_GROUP", "audit-worker"),
    auto_offset_reset="earliest",
    value_deserializer=lambda v: json.loads(v.decode()),
)
print("worker listening on orders.created", flush=True)

for msg in consumer:
    event = msg.value
    with psycopg2.connect(**DB) as conn, conn.cursor() as cur:
        cur.execute(
            "INSERT INTO order_audit (order_id, payload) VALUES (%s, %s)",
            (event["order_id"], json.dumps(event)),
        )
    print(f"audited order {event['order_id']}", flush=True)
