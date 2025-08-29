from chat import Chat, GeminiAgent, RedisHistory
from fastmcp import Client
import os, uuid, common, asyncio

async def main():
    # Load environment variables and command-line arguments
    common.load_env()
    args = common.load_args()

    # Initialize MCP client
    mcp_client = Client("src/mcpserver.py")
    async with mcp_client as client_session:
        # Initialize Redis history
        session = args["session"] if "session" in args and args["session"] is not None else str(uuid.uuid4())
        history = RedisHistory(
            redis_host=os.getenv("REDIS_HOST", "localhost"),
            redis_port=int(os.getenv("REDIS_PORT", 6379)),
            redis_db=int(os.getenv("REDIS_DB", 0)),
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
