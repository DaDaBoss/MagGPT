from sqlalchemy.orm import Session
from infrastucture.database.models.chat import Chat
from infrastucture.database.models.message import Message
from llm.base import generate


class ChatService:
    def __init__(self, db: Session):
        self.db = db

    def create_chat(self, user_id: int) -> Chat:
        chat = Chat(user_id=user_id)
        self.db.add(chat)
        self.db.commit()
        self.db.refresh(chat)
        return chat

    def get_chat(self, chat_id: int, user_id: int):
        return (
            self.db.query(Chat)
            .filter(Chat.id == chat_id, Chat.user_id == user_id)
            .first()
        )

    def get_last_chats(self, user_id: int):
        return (
            self.db.query(Chat)
            .filter(Chat.user_id == user_id)
            .order_by(Chat.id.desc())
            .limit(20)
            .all()
        )

    def get_messages(self, chat_id: int, user_id: int):
        chat = self.get_chat(chat_id, user_id)
        if not chat:
            return None

        return chat.messages

    def send_message(self, user_id: int, question: str):
        chat = self.create_chat(user_id)

        answer = generate(question)  # 🤖 LLM CALL

        message = Message(
            chat_id=chat.id,
            question=question,
            answer=answer
        )

        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)

        return message