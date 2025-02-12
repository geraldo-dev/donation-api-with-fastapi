from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, lt=100)
    active: bool
    email: EmailStr


class UserCreated(BaseModel):
    password: str = Field(..., min_length=8, max_length=20)
    created_at: datetime


class UserUpdate(BaseModel):
    name: str | None = Field(min_length=2, max_length=50)
    age: int | None = Field(gt=0, lt=100)
    active: bool | None
    email: EmailStr | None


class UserResponse(BaseModel):
    id: int
    created_at: datetime
