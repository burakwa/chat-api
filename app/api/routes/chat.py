from fastapi import APIRouter, Depends, HTTPException
from app.schemas.chat import MessageCreate, MessageResponse
from app.services.chat_service import ChatService
from app.repositories.memory import InMemoryChatRepository
from app.repositories.base import ChatRepository
from typing import List

router = APIRouter(prefix="/chat", tags=["Chat"])

# --- Dependency Injection (Bağımlılık Yönetimi) ---
# Gerçek hayatta bu veritabanı bağlantısını yöneten bir "provider" olmalıdır.
def get_repository() -> ChatRepository:
    return InMemoryChatRepository()

def get_chat_service(repo: ChatRepository = Depends(get_repository)) -> ChatService:
    return ChatService(repository=repo)

@router.post("/messages", response_model=MessageResponse, status_code=201)
async def send_message(
    payload: MessageCreate, 
    service: ChatService = Depends(get_chat_service)
):
    message = service.send_message(
        room_id=payload.room_id,
        sender=payload.sender,
        content=payload.content
    )
    return message

@router.get("/rooms/{room_id}/messages", response_model=List[MessageResponse])
async def get_room_history(
    room_id: str, 
    service: ChatService = Depends(get_chat_service)
):
    messages = service.get_room_history(room_id)
    if not messages:
        raise HTTPException(status_code=404, detail="Mesaj Bulunamadı") 
    return messages
