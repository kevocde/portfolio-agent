from pydantic import BaseModel
from google.genai import types

from .MessageDTO import MessageDTO


class HistoryDTO(BaseModel):
    session: str
    messages: list[MessageDTO]

    def convert_to_gemini_format(self) -> list[types.ContentOrDict]:
        """
        Public: Convert the history to Gemini API format.
        """
        gemini_history = []

        for msg in self.messages:
            gemini_history.append(
                types.ContentDict(
                    role=msg.role,
                    parts=[types.PartDict(text=msg.content)]
                )
            )

        return gemini_history
