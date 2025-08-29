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
                system_instruction=self.__get_system_instruction()
            )
        )

    def __get_system_instruction(self) -> str:
        system_instruction_file = os.getenv("GEMINI_SYSTEM_INSTRUCTION_FILE", "./instructions/system_instruction.md")
        if os.path.exists(system_instruction_file):
            with open(system_instruction_file, 'r') as f:
                return f.read()
        else:
            print(f"System instruction file '{system_instruction_file}' not found.")
            exit(1)

        return ""
