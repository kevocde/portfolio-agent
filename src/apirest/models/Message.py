from typing import Optional, Literal
from pydantic import BaseModel
import time

class Message(BaseModel):
    role: Optional[Literal["user", "assistant"]] = "user"
    time: Optional[float] = time.time()
    content: str
