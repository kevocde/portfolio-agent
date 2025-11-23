from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import chat_router
from common import get_env

if get_env("ENV", "development") == "production":
    app = FastAPI(docs_url=None, redoc_url=None)
else:
    app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=str(get_env("ALLOWED_ORIGINS")).split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)

@app.get("/")
async def health_check():
    return {"message": "Everything is working"}
