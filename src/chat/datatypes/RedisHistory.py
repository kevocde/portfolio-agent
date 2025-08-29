from . import BasicHistory, Message
from redis import Redis
from dataclasses import asdict
import json

class RedisHistory(BasicHistory):
    """
    Redis based chat history storage.

    Args:
        redis_host (str): Redis server host
        redis_port (int): Redis server port
        redis_db (int): Redis database number
        store_key (str): Redis list key to store chat history
    """

    def __init__(
        self,
        redis_host: str,
        redis_port: int,
        redis_db: int,
        store_key: str = "chat_history"
    ):
        super().__init__()
        self.store_key = store_key
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.redis_db = redis_db
        self.__init_redis_client(self.redis_host, self.redis_port, self.redis_db)
        self.__load_history_from_redis()

    def __init_redis_client(self, host: str, port: int, db: int):
        """
        Private: Initialize the Redis client.

        Args:
            host (str): Redis server host
            port (int): Redis server port
            db (int): Redis database number
        """
        self.client = Redis(host=host, port=port, db=db)

    def __load_history_from_redis(self):
        """
        Private: Load the history messages from Redis.
        """
        for msg in self.client.lrange(self.store_key, 0, -1):
            msg_dict = json.loads(msg)
            message = Message(role=msg_dict['role'], content=msg_dict['content'])
            super().add_message(message)

    def add_message(self, message: Message):
        """
        Public: Add a message to the history and store it in Redis.

        Args:
            message (Message): The message to add
        """
        super().add_message(message)
        self.client.rpush(self.store_key, json.dumps(asdict(message)))

    def clear_history(self):
        """
        Public: Clear the chat history both in memory and in Redis.
        """
        super().clear_history()
        self.client.delete(self.store_key)
