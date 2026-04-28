import redis

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

REFRESH_TTL = 60 * 60 * 24 * 30  # 30 days