from .RedisClient import RedisClient
from .models import History, Message

class HistoryRepository:
    """
    History repository
    """

    key_prefix = "chat.history"

    def __init__(self, redis_client: RedisClient, key: str = ""):
        self.__redis_client = redis_client
        self.__key = key

    def get_key(self) -> str:
        return ".".join([HistoryRepository.key_prefix, self.__key])

    def get_history(self) -> History:
        messages = []

        for msg in self.__redis_client.get_key(self.get_key()):
            messages.append(Message(role=msg['role'], time=msg['time'], content=msg['content']))

        return History(session=self.__key, messages=messages)

    def add_message(self, message: Message):
        self.__redis_client.add_to_key(self.get_key(), message.model_dump())
