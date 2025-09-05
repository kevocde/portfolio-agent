import uuid, time, os
import uvicorn, common
from typing import Union
from fastapi import FastAPI
from apirest import Message, History, RedisClient, HistoryRepository


common.load_env()

redis_client = RedisClient(host=common.get_env("REDIS_HOST"), port=int(common.get_env("REDIS_PORT")), db=int(common.get_env("REDIS_DB")))
app = FastAPI()

@app.get("/")
async def help_check():
    return {"code": 200, "errors": False}

@app.post("/chat")
async def init_chat():
    return {"session": str(uuid.uuid4()), "messages": [{"role": "assistance", "time": time.time(), "text": "¡Hola!, que bueno tenerte por aquí, soy Kevin AI, puedes preguntarme lo que desees"}]}

@app.post("/chat/{session}")
async def send_message_to_chat(session: str, message: Message) -> Message:
    history_repository = HistoryRepository(redis_client, session)
    history_repository.add_message(message)

    return Message(role="assistant", content="This is a placeholder response.")

@app.get("/chat/{session}")
async def get_chat_history(session: str) -> History:
    history_repository = HistoryRepository(redis_client, session)
    return history_repository.get_history()

"""
if __name__ == "__main__":
    args = common.load_args()

    uvicorn.run(
        app,
        host=args['host'],
        port=args['port']
    )
"""