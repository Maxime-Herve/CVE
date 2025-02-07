FROM python:3.9-slim

WORKDIR /app

COPY main.py cves.py products.py .

RUN pip install --no-cache-dir fastapi uvicorn

EXPOSE 10000

CMD ["python3", "main.py"]
