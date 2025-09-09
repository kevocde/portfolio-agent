import time

from pydantic import BaseModel
from typing import Annotated

from ..constans import ROLE_USER


class MessageDTO(BaseModel):
    role: str = ROLE_USER
    time: float = time.time()
    content: str
