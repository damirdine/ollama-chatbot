import json
import httpx

from dotenv import DotEnv

from fastapi.responses import StreamingResponse
from fastapi import APIRouter, Request

from app.schemas.chat import ChatRequest
from app.services.chat_services import ChatService
from app.domain.models import Conversation

dotenv = DotEnv()
router = APIRouter()
chat_service = ChatService()

OLLAMA_API_URL = dotenv.get("OLLAMA_API_URL")
DEFAULT_MODEL = dotenv.get("DEFAULT_MODEL")


@router.post("/chat")
async def chat_endpoint(request: Request, payload: ChatRequest):
    conv: Conversation
    if not payload.conversation_id:
        conv = chat_service.create_conversation()
    else:
        conv = chat_service.get_conversation(payload.conversation_id)
        if not conv:
            raise HTTPException(status_code=404, detail="Conversation not found")

    chat_service.add_user_message(conv, payload.message)

    ollama_payload = {
        "model": DEFAULT_MODEL,
        "messages": [m.dict() for m in conv.messages],
        "stream": True
    }

    async def event_stream():
        response_text = ""
        async with httpx.AsyncClient(timeout=None) as client:
            async with client.stream("POST", OLLAMA_API_URL, json=ollama_payload) as response:
                async for line in response.aiter_lines():
                    if not line.strip():
                        continue
                    try:
                        data = line.removeprefix("data: ").strip()
                        if data == "[DONE]":
                            break
                        chunk = json.loads(data)["message"]["content"]
                        response_text += chunk
                        yield f"data: {chunk}\n\n"
                    except Exception as e:
                        yield f"data: [ERROR] {str(e)}\n\n"

        chat_service.add_assistant_message(conv, response_text)

    return StreamingResponse(event_stream(), media_type="text/event-stream", headers={"X-Conversation-ID": conv.id})
