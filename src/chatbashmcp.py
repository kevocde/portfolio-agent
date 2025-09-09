import os
import uuid
import asyncio

from common import RedisHistoryRepository, RedisClient, get_env, load_args

from chat import Chat, GeminiAgent
from fastmcp import Client

from common.Repositories import RedisHistoryRepository


async def main():
    # Load environment variables and command-line arguments
    args = load_args()

    # Initialize MCP client
    mcp_client = Client("src/mcpserver.py")
    async with mcp_client as client_session:
        # Initialize Redis history
        session = args["session"] if "session" in args and args["session"] is not None else str(uuid.uuid4())

        history_repository = RedisHistoryRepository(
            client=RedisClient(
                host=get_env("REDIS_HOST", "localhost"),
                port=int(get_env("REDIS_PORT", 6379)),
                db=int(get_env("REDIS_DB", 0)),
            ),
            key=session
        )

        print("History Key: {}".format(session))

        # Initialize chat with Gemini agent and Redis history
        chat = Chat(GeminiAgent(client_session), history_repository)

        # Start chat loop
        while True:
            message = input("you: ")
            if message.lower() in {"/q", "/quit"}:
                break

            if message.lower() in {"/h", "/history"}:
                print(chat.get_history())
                continue

            response = await chat.answer(message)
            print(response.content)

if __name__ == "__main__":
    asyncio.run(main())
