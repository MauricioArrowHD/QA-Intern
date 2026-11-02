FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir flask==3.0.3 psycopg2-binary==2.9.9 redis==5.0.8 kafka-python==2.0.2
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
