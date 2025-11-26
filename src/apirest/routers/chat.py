import uuid, time

from typing import Any

from fastapi.responses import FileResponse
from fastmcp import Client
from fastapi import APIRouter, Depends

from common import RedisClient, RedisHistoryRepository, MessageDTO, InMessageDTO, get_env
from apirest.middlewares import AnonymousGuardDependency
from chat import Chat, GeminiAgent


# Initialize Redis client
redis_client = RedisClient(
    host=get_env("REDIS_HOST"),
    port=int(get_env("REDIS_PORT")),
    db=int(get_env("REDIS_DB"))
)

# Initialize the mcp client
mcp_client = Client("src/mcpserver.py")

# Initialize the anonymous guard
anonymous_guard = AnonymousGuardDependency(redis_client)

# Initialize the router
router = APIRouter(prefix="/chat", dependencies=[Depends(anonymous_guard)])

@router.get("")
async def get_chat_umd():
    """
    Get the chat umd
    """
    return FileResponse("public/dist/chat-widget.umd.js")

@router.post("")
async def init_chat() -> dict[Any, Any]:
    """
    Initialize the chat
    """
    return {
        "session": str(uuid.uuid4()),
        "messages": [
            MessageDTO(
                role="assistance",
                time=time.time(),
                content="¡Hola!, que bueno tenerte por aquí, soy Kevin AI, puedes preguntarme lo que desees"
            ),
        ]
    }

@router.get("/{session}")
async def get_chat_history(session: str):
    """
    Get the chat history
    """
    return get_history_repo(session).get_history()

@router.post("/{session}", dependencies=[Depends(anonymous_guard)])
async def send_message_to_chat(session: str, message: InMessageDTO) -> MessageDTO:
    """
    Send a message to the chat
    """
    async with mcp_client as client_session:
        gemini_agent = GeminiAgent(client_session)
        chat = Chat(gemini_agent, get_history_repo(session))
        return await chat.answer(message.to_message_dto().content)

def get_history_repo(session: str) -> RedisHistoryRepository:
    """
    Get the history repository
    """
    return RedisHistoryRepository(client=redis_client, key="chat.history.{}".format(session))
