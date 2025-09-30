
# Easy-Deploy

*A lightweight, mini-Vercel built with Django, Celery, Redis, and AWS S3.*

[![Django](https://img.shields.io/badge/Django-4.x-green.svg)](https://www.djangoproject.com/)
[![Celery](https://img.shields.io/badge/Celery-5.x-brightgreen.svg)](https://docs.celeryq.dev/)
[![Redis](https://img.shields.io/badge/Redis-7.x-red.svg)](https://redis.io/)
[![AWS S3](https://img.shields.io/badge/AWS-S3-orange.svg)](https://aws.amazon.com/s3/)

---

## 📖 Overview

**Easy-Deploy** is a simplified deployment system inspired by **Vercel**.
It provides:

* A service to **upload code repositories**.
* A service to **process and deploy builds** asynchronously.
* A **request handler** that serves deployed content directly from AWS S3.

This project uses **Django**, **Celery**, **Redis**, **GitPython**, and **boto3** to create a smooth deployment pipeline.

---

## ✅ Progress Tracker

### 📦 Upload-Service (Django)

* ✅ Install Python and Django
* ✅ Start a new Django project and app
* ✅ Configure Django settings for your app
* ✅ Install required dependencies: `django`, `celery`, `redis`, `boto3`, `gitpython`
* ✅ Set up Celery with Redis as the broker
* ✅ Create a Django view to accept a repository URL
* ✅ Generate a unique session ID for each upload request
* ✅ Clone repositories using **GitPython** → `/out/<session_id>`
* ✅ List all file paths in the cloned folder
* ✅ Configure AWS credentials with **boto3**
* ✅ Upload files to S3 via **boto3**
* ✅ Upload files asynchronously with Celery tasks
* ✅ Store upload status in Redis
* ✅ Expose an API endpoint to check upload status

---

### ⚙️ Deploy-Service (Django)

* ❌ Create a Django management command / Celery worker to process uploads from Redis queue
* ❌ Download files from S3 using **boto3**
* ❌ (Optional) Integrate Django static files system or containerize build process
* ❌ Upload processed directories back to S3
* ❌ Update Redis to mark uploads as **processed**

---

### 🌐 Request-Handler (Django)

* ❌ Create a Django view to handle incoming requests
* ❌ Parse subdomain or request params → identify **session ID**
* ❌ Retrieve deployed files from S3 via **boto3**
* ❌ Serve files with correct **Content-Type headers** (e.g., `text/html`)

---

## ⚡ Tech Stack

* **Backend** → Django + Django REST Framework
* **Task Queue** → Celery + Redis
* **Version Control** → GitPython
* **Storage** → AWS S3 via boto3
* **Deployment** → Docker (optional)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/GauravTheBeginner/easy-deployment.git
cd easy-deploy
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start Redis & Celery

```bash
redis-server
celery -A your_project worker -l info
```

### 4. Run Django

```bash
python manage.py runserver
```

---

## 📌 Roadmap

* [ ] Add CI/CD pipeline
* [ ] Add frontend dashboard for uploads & status tracking
* [ ] Add multi-cloud support (GCP, Azure)
* [ ] Custom domain + SSL integration

---

## 🛡️ License

MIT License © 2025 — Built for learning & experimentation.

---
