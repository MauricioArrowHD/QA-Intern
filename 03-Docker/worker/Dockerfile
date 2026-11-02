FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir psycopg2-binary==2.9.9 kafka-python==2.0.2
COPY worker.py .
CMD ["python", "worker.py"]
