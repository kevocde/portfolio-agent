import uuid, time

import uvicorn, common
from fastmcp import Client
from fastapi import FastAPI

from common import RedisClient, RedisHistoryRepository, HistoryDTO, MessageDTO, InMessageDTO, load_args
from chat import Chat, GeminiAgent

# Initialize Redis client
redis_client = RedisClient(host=common.get_env("REDIS_HOST"), port=int(common.get_env("REDIS_PORT")), db=int(common.get_env("REDIS_DB")))

# Initialize the mcp client
mcp_client = Client("src/mcpserver.py")

# Initialize the gemini agent
gemini_agent = GeminiAgent(mcp_client)

# Initialize the api rest
app = FastAPI()

@app.get("/")
async def help_check():
    return {"code": 200, "errors": False}

@app.post("/chat")
async def init_chat():
    session = str(uuid.uuid4())
    return {"session": str(uuid.uuid4()), "messages": [{"role": "assistance", "time": time.time(), "text": "¡Hola!, que bueno tenerte por aquí, soy Kevin AI, puedes preguntarme lo que desees"}]}

@app.post("/chat/{session}")
async def send_message_to_chat(session: str, message: InMessageDTO) -> MessageDTO:
    async with mcp_client as client_session:
        gemini_agent = GeminiAgent(client_session)
        redis_history_repository = RedisHistoryRepository(client=redis_client, key="chat.history.{}".format(session))
        chat = Chat(gemini_agent, redis_history_repository)
        message_dto = message.to_message_dto()
        response = await chat.answer(message_dto.content)
        return response

@app.get("/chat/{session}")
async def get_chat_history(session: str) -> HistoryDTO:
    redis_history_repository = RedisHistoryRepository(client=redis_client, key="chat.history.{}".format(session))
    return redis_history_repository.get_history()

if __name__ == "__main__":
    args = load_args()

    uvicorn.run(
        app,
        host=args['host'],
        port=args['port']
    )
