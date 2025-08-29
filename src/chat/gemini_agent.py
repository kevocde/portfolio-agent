from .datatypes import BasicHistory, Message
from .ai_agent import AiAgent
from .constans import ROLE_ASSISTANT
from google import genai
from google.genai import types
from fastmcp import Client
import os, asyncio

class GeminiAgent(AiAgent):
    def __init__(self, mcp_client: Client|None = None):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.mcp_client = mcp_client

    async def get_completion(self, history: BasicHistory) -> Message:
        response = await self.__generate_content_async(history)
        return Message(role=ROLE_ASSISTANT, content=str(response.text).rstrip("\n"))

    async def __generate_content_async(self, history: BasicHistory) -> types.GenerateContentResponse:
        tools = []

        if self.mcp_client:
            tools.append(self.mcp_client.session)

        return await self.client.aio.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-2.0-flash"),
            contents=history.convert_to_gemini_format(),
            config=genai.types.GenerateContentConfig(
                temperature=0,
                tools=tools,
            )
        )
