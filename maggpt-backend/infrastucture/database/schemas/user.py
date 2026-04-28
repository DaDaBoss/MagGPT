from pydantic import BaseModel


class UserCreate(BaseModel):
    login: str
    password: str = Field(..., min_length=6, max_length=72)

class UserRead(BaseModel):
    id: int
    login: str

    class Config:
        from_attributes = True