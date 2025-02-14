from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    age: int = 0


class UserCreated(UserBase):
    password: str = Field(..., min_length=4, max_length=20)


class Userlogin(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=4, max_length=20)


class UserUpdate(BaseModel):
    name: str | None = Field(min_length=2, max_length=50)
    age: int | None = Field(gt=0, lt=100)
    is_active: bool | None
    email: EmailStr | None


class UserResponse(UserBase):
    id: int
    created_at: datetime
