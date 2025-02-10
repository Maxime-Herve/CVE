FROM python:3.10.16-slim

WORKDIR /app

COPY requirements.txt main.py filtering.py products.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 10000

CMD ["python3", "main.py"]
