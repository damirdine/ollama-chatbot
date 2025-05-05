from typing import List, Optional
from app.domain.models import Conversation, Message
import uuid

class ChatService:
    def __init__(self):
        self.conversations: List[Conversation] = []

    def get_conversation(self, conv_id: str) -> Optional[Conversation]:
        return next((c for c in self.conversations if c.id == conv_id), None)

    def create_conversation(self) -> Conversation:
        conv = Conversation(id=str(uuid.uuid4()))
        self.conversations.append(conv)
        return conv

    def add_user_message(self, conv: Conversation, content: str):
        conv.messages.append(Message(role="user", content=content))

    def add_assistant_message(self, conv: Conversation, content: str):
        conv.messages.append(Message(role="assistant", content=content))
