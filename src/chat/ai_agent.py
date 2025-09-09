import time

from common import HistoryDTO, MessageDTO
from common import ROLE_ASSISTANT

class AiAgent:
    async def get_completion(self, history: HistoryDTO) -> MessageDTO:
        return MessageDTO(role=ROLE_ASSISTANT, time=time.time(), content="This is a placeholder response.")
