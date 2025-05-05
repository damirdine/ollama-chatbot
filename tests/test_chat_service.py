from app.services.chat_services import ChatService
import pytest

@pytest.fixture
def chat_service():
    return ChatService()

def test_create_conversation(chat_service):
    conv = chat_service.create_conversation()
    assert conv.id
    assert conv.messages == []

def test_add_user_and_assistant_message(chat_service):
    conv = chat_service.create_conversation()
    chat_service.add_user_message(conv, "Hello")
    chat_service.add_assistant_message(conv, "Hi there!")
    assert len(conv.messages) == 2
    assert conv.messages[0].role == "user"
    assert conv.messages[1].role == "assistant"
