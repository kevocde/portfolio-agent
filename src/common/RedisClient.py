import json
import redis
from typing import Any


class RedisClient:
    """
    Redis client
    """

    def __init__(self, host: str, port: int, db: int):
        self.client = redis.Redis(host=host, port=port, db=db)

    def get_client(self) -> redis.Redis:
        return self.client

    def get_key(self, key: str) -> list[Any]:
        return [json.loads(msg) for msg in self.client.lrange(key, 0, -1)]

    def add_to_key(self, key: str, value: dict):
        self.client.rpush(key, json.dumps(value))

    def replace_key(self, key: str, idx: int, value: dict):
        self.client.lset(key, idx, json.dumps(value))

    def delete_key(self, key: str):
        self.client.delete(key)
