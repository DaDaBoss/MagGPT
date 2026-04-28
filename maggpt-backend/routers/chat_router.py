from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from infrastucture.database.database import get_db
from services.chat_service import ChatService
from auth.deps import get_current_user

router = APIRouter(prefix="/chat", tags=["Chat"])


def get_service(db: Session = Depends(get_db)):
    return ChatService(db)


# создать чат вручную (если нужно)
@router.post("/")
def create_chat(
    user_id: int = Depends(get_current_user),
    service: ChatService = Depends(get_service)
):
    return service.create_chat(user_id)


# получить чат (с проверкой владельца)
@router.get("/{chat_id}")
def get_chat(
    chat_id: int,
    user_id: int = Depends(get_current_user),
    service: ChatService = Depends(get_service)
):
    chat = service.get_chat(chat_id, user_id)
    if not chat:
        raise HTTPException(404, "Chat not found")
    return chat


# последние 20 чатов
@router.get("/")
def get_last_chats(
    user_id: int = Depends(get_current_user),
    service: ChatService = Depends(get_service)
):
    return service.get_last_chats(user_id)


# сообщения чата
@router.get("/{chat_id}/messages")
def get_messages(
    chat_id: int,
    user_id: int = Depends(get_current_user),
    service: ChatService = Depends(get_service)
):
    messages = service.get_messages(chat_id, user_id)

    if messages is None:
        raise HTTPException(404, "Chat not found")

    return messages


# отправить сообщение (создаёт чат)
@router.post("/message")
def send_message(
    question: str,
    user_id: int = Depends(get_current_user),
    service: ChatService = Depends(get_service)
):
    return service.send_message(user_id, question)