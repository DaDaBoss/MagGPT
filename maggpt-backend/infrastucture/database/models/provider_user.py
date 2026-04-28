from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from infrastucture.database.database import Base


class ProviderUser(Base):
    __tablename__ = "provider_users"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    provider = Column(String, nullable=False)
    provider_user_id = Column(String, nullable=False)

    user = relationship("User", backref="providers")

    __table_args__ = (
        UniqueConstraint("provider", "provider_user_id"),
    )