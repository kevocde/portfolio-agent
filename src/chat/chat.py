from .ai_agent import AiAgent
from .datatypes import BasicHistory, Message
from .constans import ROLE_USER

class Chat:
    def __init__(self, ai_agent: AiAgent, history: BasicHistory|None = None):
        self.ai_agent = ai_agent
        self.history = history

    async def answer(self, message: str, history: BasicHistory = BasicHistory()) -> Message:
        if not self.history:
            self.history = history

        message_obj = Message(role=ROLE_USER, content=message)
        self.history.add_message(message_obj)
        agent_response = await self.ai_agent.get_completion(self.history)
        self.history.add_message(agent_response)

        return agent_response

    def get_history(self) -> BasicHistory|None:
        return self.history
