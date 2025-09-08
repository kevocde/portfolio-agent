from pydantic import BaseModel


class MessageDTO(BaseModel):
    role: str
    time: float
    content: str
