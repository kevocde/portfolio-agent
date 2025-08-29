from .datatypes import BasicHistory, Message
from .constans import ROLE_ASSISTANT

class AiAgent:
    async def get_completion(self, history: BasicHistory) -> Message:
        return Message(role=ROLE_ASSISTANT, content="This is a placeholder response.")
