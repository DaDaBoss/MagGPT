import uuid

from sqlalchemy.orm import Session

from infrastucture.database.models.user import User
from infrastucture.database.models.provider_user import ProviderUser

from auth.security import (
    hash_password,
    verify_password,
    create_access_token,
)

from infrastucture.redis.redis_client import redis_client, REFRESH_TTL


class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def register(self, login: str, password: str | None):
        user = self.db.query(User).filter(User.login == login).first()
        if user:
            raise ValueError("Login already exists")

        user = User(
            login=login,
            hashed_password=hash_password(password) if password else None
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def login(self, login: str, password: str):
        user = self.db.query(User).filter(User.login == login).first()

        if not user or not user.hashed_password:
            return None

        if not verify_password(password, user.hashed_password):
            return None

        return self._issue_tokens(user.id)

    def oauth_login(self, provider: str, provider_user_id: str, login: str):
        link = self.db.query(ProviderUser).filter(
            ProviderUser.provider == provider,
            ProviderUser.provider_user_id == provider_user_id
        ).first()

        if link:
            return self._issue_tokens(link.user_id)

        user = self.db.query(User).filter(User.login == login).first()

        if not user:
            user = User(login=login)
            self.db.add(user)
            self.db.flush()

        link = ProviderUser(
            user_id=user.id,
            provider=provider,
            provider_user_id=provider_user_id
        )

        self.db.add(link)
        self.db.commit()

        return self._issue_tokens(user.id)

    def refresh(self, refresh_token: str):
        user_id = redis_client.get(f"refresh:{refresh_token}")

        if not user_id:
            return None

        return self._issue_tokens(int(user_id))

    def _issue_tokens(self, user_id: int):
        access_token = create_access_token({"sub": str(user_id)})

        refresh_token = str(uuid.uuid4())

        redis_client.setex(
            f"refresh:{refresh_token}",
            REFRESH_TTL,
            user_id
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }