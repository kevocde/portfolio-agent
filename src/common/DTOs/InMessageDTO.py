import time

from pydantic import BaseModel, Field
from typing import Annotated

from .MessageDTO import MessageDTO
from ..constans import ROLE_USER
from common import get_message_length


class InMessageDTO(BaseModel):
    content: Annotated[str, Field(min_length=get_message_length()[0], max_length=get_message_length()[1])]

    def to_message_dto(self) -> MessageDTO:
        return MessageDTO(role=ROLE_USER, time=time.time(), content=self.content)
