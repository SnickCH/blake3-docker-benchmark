FROM python:3.11-slim

RUN pip install --no-cache-dir blake3

WORKDIR /app
COPY hash_benchmark.py .

VOLUME ["/results"]

CMD ["python", "hash_benchmark.py"]
