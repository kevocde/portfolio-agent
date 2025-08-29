from dataclasses import dataclass
from google.genai import types
from .Message import Message

@dataclass
class BasicHistory:
    """
    Basic in-memory chat history storage.

    Note: While the program is running, the history is stored in memory.
    """

    def __init__(self):
        self.__messages: list[Message] = []

    def add_message(self, message: Message):
        """
        Public: Add a message to the history.

        Args:
            message (Message): The message to add
        """
        self.__messages.append(message)

    def get_messages(self) -> list[Message]:
        """
        Public: Get all messages in the history.
        """
        return self.__messages

    def clear_history(self):
        """
        Public: Clear the chat history.
        """
        self.__messages = []

    def convert_to_gemini_format(self) -> list[types.ContentOrDict]:
        """
        Public: Convert the history to Gemini API format.
        """
        gemini_history = []

        for msg in self.__messages:
            gemini_history.append(
                types.ContentDict(
                    role=msg.role,
                    parts=[types.PartDict(text=msg.content)]
                )
            )

        return gemini_history
