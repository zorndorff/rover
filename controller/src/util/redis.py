import redis
import os

def connect:
  r = redis.Redis(os.environ['REDIS_URL'];
  return r

    