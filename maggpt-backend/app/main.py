from fastapi import FastAPI

from routers.user_router import router as user_router
from routers.auth_router import router as auth_router
from routers.github_router import router as github_router
from routers.chat_router import router as chat_router


app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(github_router)
app.include_router(chat_router)