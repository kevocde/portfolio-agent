import os
import uuid
import asyncio

import common

from chat import Chat, GeminiAgent, RedisHistory
from fastmcp import Client


async def main():
    # Load environment variables and command-line arguments
    args = common.load_args()

    # Initialize MCP client
    mcp_client = Client("src/mcpserver.py")
    async with mcp_client as client_session:
        # Initialize Redis history
        session = args["session"] if "session" in args and args["session"] is not None else str(uuid.uuid4())
        history = RedisHistory(
            redis_host=common.get_env("REDIS_HOST", "localhost"),
            redis_port=int(common.get_env("REDIS_PORT", 6379)),
            redis_db=int(common.get_env("REDIS_DB", 0)),
            store_key=session
        )
        print("History Key: {}".format(session))

        # Initialize chat with Gemini agent and Redis history
        chat = Chat(GeminiAgent(client_session), history)

        # Start chat loop
        while True:
            message = input("you: ")
            if message.lower() in {"exit", "quit"}:
                break
            print(await chat.answer(message))

if __name__ == "__main__":
    asyncio.run(main())
