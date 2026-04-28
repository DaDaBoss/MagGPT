from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from infrastucture.database.database import get_db
from services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


def get_service(db: Session = Depends(get_db)):
    return AuthService(db)


@router.post("/register")
def register(login: str, password: str | None, service: AuthService = Depends(get_service)):
    try:
        return service.register(login, password)
    except ValueError as e:
        raise HTTPException(400, str(e))


@router.post("/login")
def login(login: str, password: str, service: AuthService = Depends(get_service)):
    tokens = service.login(login, password)
    if not tokens:
        raise HTTPException(401, "Invalid credentials")
    return tokens


@router.post("/refresh")
def refresh(refresh_token: str, service: AuthService = Depends(get_service)):
    tokens = service.refresh(refresh_token)
    if not tokens:
        raise HTTPException(401, "Invalid refresh token")
    return tokens