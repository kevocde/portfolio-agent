import time

from pydantic import BaseModel, Field
from typing import Annotated

from .MessageDTO import MessageDTO
from ..constans import ROLE_USER
from common import get_env


class InMessageDTO(BaseModel):
    content: Annotated[str, Field(min_length=10, max_length=int(get_env("MAX_MESSAGE_LENGTH", 400)))]

    def to_message_dto(self) -> MessageDTO:
        return MessageDTO(role=ROLE_USER, time=time.time(), content=self.content)
