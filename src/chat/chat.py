import time

from common import HistoryRepository, MessageDTO, HistoryDTO

from .ai_agent import AiAgent
from common import ROLE_USER

class Chat:
    def __init__(self, ai_agent: AiAgent, history: HistoryRepository):
        self.__ai_agent = ai_agent
        self.__history = history

    async def answer(self, message: str) -> MessageDTO:
        message_obj = MessageDTO(role=ROLE_USER, time=time.time(), content=message)
        self.__history.add_message(message_obj)
        agent_response = await self.__ai_agent.get_completion(self.__history.get_history())
        self.__history.add_message(agent_response)

        return agent_response

    def get_history(self) -> HistoryDTO|None:
        return self.__history.get_history()
