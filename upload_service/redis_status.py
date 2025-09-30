import redis
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
r = redis.Redis.from_url(REDIS_URL)

def set_upload_status(session_id, status):
    r.set(f"upload_status:{session_id}", status)

def get_upload_status(session_id):
    return r.get(f"upload_status:{session_id}")
