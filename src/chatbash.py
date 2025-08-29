from chat import Chat, GeminiAgent, RedisHistory
import os, uuid, common, asyncio

async def main():
    # Load environment variables and command-line arguments
    common.load_env()
    args = common.load_args()

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
    chat = Chat(GeminiAgent(), history)

    # Start chat loop
    while True:
        message = input("you: ")
        if message.lower() in {"exit", "quit"}:
            break

        message = await chat.answer(message)
        print(message)

if __name__ == "__main__":
    asyncio.run(main())
