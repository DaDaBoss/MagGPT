from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from infrastucture.database.database import get_db
from services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


def get_service(db: Session = Depends(get_db)):
    return UserService(db)


@router.get("/{user_id}")
def get_user(user_id: int, service: UserService = Depends(get_service)):
    return service.get_by_id(user_id)