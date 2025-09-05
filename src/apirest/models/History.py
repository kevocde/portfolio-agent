from typing import Optional
from .Message import Message
from pydantic import BaseModel

class History(BaseModel):
    session: str
    messages: list[Message]