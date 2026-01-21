FROM python:3.13-slim

WORKDIR /app

# Install build dependencies for native extensions
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    libc6-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./src ./src/

ENV PYTHONPATH=/app

EXPOSE 9002

CMD ["python", "src/app.py"]
