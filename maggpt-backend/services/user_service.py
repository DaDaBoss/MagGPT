from sqlalchemy.orm import Session
from infrastucture.database.models.user import User


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def create(self, login: str, hashed_password: str | None = None):
        user = User(
            login=login,
            hashed_password=hashed_password
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user