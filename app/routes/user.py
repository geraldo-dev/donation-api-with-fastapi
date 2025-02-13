from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db, SessionLocal
from typing import Annotated
from app.cruds.user import check_email, created_new_user, get_user
from app.models.user import User
from app.schemas.user import UserResponse, UserCreated

router = APIRouter()

SessionDp = Annotated[Session, Depends(get_db)]


@router.get('/{user_id}', status_code=200, response_model=UserResponse)
def get_by_user(db: SessionDp, user_id: int):
    user: User | bool = get_user(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user


@router.post('/', status_code=201, response_model=UserResponse)
def create_user(db: SessionDp, user: UserCreated):

    existing_user = check_email(db, user.email)

    if existing_user:
        raise HTTPException(status_code=400, detail='email already registered')

    return created_new_user(db=db, user=user)
