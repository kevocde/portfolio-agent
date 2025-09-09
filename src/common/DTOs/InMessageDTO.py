import time

from pydantic import BaseModel

from .MessageDTO import MessageDTO
from ..constans import ROLE_USER


class InMessageDTO(BaseModel):
    content: str

    def to_message_dto(self) -> MessageDTO:
        return MessageDTO(role=ROLE_USER, time=time.time(), content=self.content)
