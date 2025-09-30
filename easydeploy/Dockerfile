# Dockerfile for Django backend
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install git
RUN apt-get update -y && apt-get install -y \ 
    build-essential \
    procps \
    libodbc2 \
    odbcinst \
    curl \
    gnupg \
    unixodbc \
    unixodbc-dev && \
    rm -rf /var/lib/apt/lists/*


COPY easydeploy/requirements.txt ./requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "easydeploy.wsgi:application", "--bind", "0.0.0.0:8000"]
