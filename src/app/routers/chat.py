import uuid
import time

from fastmcp import Client
from fastapi import APIRouter

from common import RedisClient, RedisHistoryRepository, MessageDTO, InMessageDTO, get_env
from chat import Chat, GeminiAgent


# Initialize Redis client
redis_client = RedisClient(
    host=get_env("REDIS_HOST"),
    port=int(get_env("REDIS_PORT")),
    db=int(get_env("REDIS_DB"))
)

# Initialize the mcp client
mcp_client = Client("src/mcpserver.py")

# Initialize the router
router = APIRouter(prefix="/chat")

@router.post("/")
async def init_chat():
    """
    Initialize the chat
    """
    return {"session": str(uuid.uuid4()), "messages": [{"role": "assistance", "time": time.time(), "text": "¡Hola!, que bueno tenerte por aquí, soy Kevin AI, puedes preguntarme lo que desees"}]}

@router.post("/{session}")
async def send_message_to_chat(session: str, message: InMessageDTO) -> MessageDTO:
    """
    Send a message to the chat
    """
    async with mcp_client as client_session:
        gemini_agent = GeminiAgent(client_session)
        chat = Chat(gemini_agent, get_history_repo(session))
        return await chat.answer(message.to_message_dto().content)

@router.get("/{session}")
async def get_chat_history(session: str):
    """
    Get the chat history
    """
    return get_history_repo(session).get_history()

def get_history_repo(session: str) -> RedisHistoryRepository:
    """
    Get the history repository
    """
    return RedisHistoryRepository(client=redis_client, key="chat.history.{}".format(session))
