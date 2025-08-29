from dataclasses import dataclass

@dataclass
class Message:
    role: str
    content: str

    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

    def __str__(self) -> str:
        content = self.content.rstrip('\n\r')
        return f"{self.role}: {content}"