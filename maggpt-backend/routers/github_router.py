from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from auth.providers.provider_github import oauth
from infrastucture.database.database import get_db
from services.auth_service import AuthService

router = APIRouter(prefix="/auth/github", tags=["GitHub"])


@router.get("/login")
async def login(request: Request):
    redirect_uri = "http://localhost:8000/auth/github/callback"
    return await oauth.github.authorize_redirect(request, redirect_uri)


@router.get("/callback")
async def callback(request: Request, db: Session = Depends(get_db)):
    token = await oauth.github.authorize_access_token(request)
    resp = await oauth.github.get("user", token=token)
    profile = resp.json()

    service = AuthService(db)

    return service.oauth_login(
        provider="github",
        provider_user_id=str(profile["id"]),
        login=profile["login"]
    )