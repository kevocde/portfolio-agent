from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from .routers import chat_router
from .middlewares import AnonymousGuard
from common import RedisClient, get_env

redis_client = RedisClient(
    host=get_env("REDIS_HOST"),
    port=int(get_env("REDIS_PORT")),
    db=int(get_env("REDIS_DB"))
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=str(get_env("ALLOWED_ORIGINS")).split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.middleware("http")
async def add_middleware(request: Request, call_next):
    middleware = AnonymousGuard(app, redis_client)
    return await middleware(request, call_next)

app.include_router(chat_router)
