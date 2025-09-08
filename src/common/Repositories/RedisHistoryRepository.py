from common.DTOs import HistoryDTO, MessageDTO
from .HistoryRepository import HistoryRepository
from ..RedisClient import RedisClient


class RedisHistoryRepository(HistoryRepository):
    """
    Redis history repository
    """

    def __init__(self, client: RedisClient, key: str = ""):
        self.__client = client
        self.__key = key

    def get_history(self) -> HistoryDTO:
        """
        Public: get the history dtos
        """
        messages = [MessageDTO(role=msg['role'], time=msg['time'], content=msg['content']) for msg in self.__client.get_key(self.__key)]
        return HistoryDTO(session=self.__key, messages=messages)


    def add_message(self, message: MessageDTO):
        """
        Public: add a message to the history
        """
        self.__client.add_to_key(self.__key, message.model_dump())

    def clear_history(self):
        """
        Public: clear the history
        """
        self.__client.delete_key(self.__key)
