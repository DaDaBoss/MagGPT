from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

from infrastucture.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    login = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=True)

    chats = relationship("Chat", backref="user")