from .MessageDTO import MessageDTO
from pydantic import BaseModel


class HistoryDTO(BaseModel):
    session: str
    messages: list[MessageDTO]
