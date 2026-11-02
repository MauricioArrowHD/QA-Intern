# Ejercicio 1: Docker (25 min)

Puedes usar internet y AI. **Lo importante es que expliques tu razonamiento en voz alta.**
Requisitos: Docker Desktop y un editor. Trabaja desde esta carpeta.

## Parte A: "No funciona"
Tienes una pequeña tienda: una `api`, una base de datos `db` (Postgres) y un `cache` (Redis).

```bash
docker compose up -d --build
```

La API debería responder en `http://localhost:8080/health` con `db: ok` y `cache: ok`, y los datos de la base de datos deben sobrevivir a un `docker compose down` + `up`.

1. Averigua por qué no funciona (hay más de un problema).
2. Explica la causa de cada uno, no solo el arreglo.
3. Demuestra que quedó bien.

Baja el stack antes de la Parte B: `docker compose down -v`.

## Parte B: "Necesitamos avisar cuando se crea una orden"
Cuando se crea una orden (`POST /orders`) hay que guardar una auditoría y notificar, **sin que la API espere** a que eso termine.

1. Sin mirar el código: dibuja o explica cómo lo resolverías con un *message broker* (por ejemplo Kafka). ¿Quién envía, quién recibe, qué se agrega al compose, en qué red va y qué datos necesitan persistir?
2. Ya tenemos una primera versión en `docker-compose.kafka.yml`. Levántala y haz que el flujo funcione:
   ```bash
   docker compose -f docker-compose.kafka.yml up -d --build
   curl -X POST localhost:8080/orders -H 'content-type: application/json' \
        -d '{"user_id":1,"items":[{"product_id":1,"qty":1}]}'
   ```
   Una orden bien procesada aparece en la tabla `order_audit`.
3. Como QA: ¿qué pruebas harías a este flujo asíncrono?
