import time
from fastapi import status, Response, Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.types import ASGIApp, Receive, Scope, Send

from common.RedisClient import RedisClient
from common import get_env


class AnonymousGuardDependency:

    def __init__(self, redis_client: RedisClient):
        self.__redis_client = redis_client

    async def __call__(self, request: Request):
        access_list = self.__redis_client.get_key("anonymous_access")
        client_address = request.scope["client"][0]
        now = time.time()
        max_tries = int(get_env("MAX_TRIES", 10))
        max_time = int(get_env("MAX_TIME", 60 * 60))

        added_to_access = True
        for idx, value in enumerate(access_list):
            if value["address"] == client_address:
                added_to_access = False

                if value["tries"] >= max_tries and now <= (value["time"] + max_time):
                    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Max tries reached, try again later")
                else:
                    self.__redis_client.replace_key("anonymous_access", idx, {"address": client_address, "time": time.time(), "tries": value["tries"] + 1})

                break

        if added_to_access:
            self.__redis_client.add_to_key("anonymous_access", {"address": client_address, "time": time.time(), "tries": 0})
