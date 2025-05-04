FROM python:3.9-alpine  # 5x smaller than "slim"

WORKDIR /app

# Install minimal dependencies
RUN apk add --no-cache g++ make libffi-dev openssl-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["/bin/sh", "-c", "uvicorn punctuation_service:app --host 0.0.0.0 --port $PORT"]
