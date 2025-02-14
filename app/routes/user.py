from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from typing import Annotated
from app.cruds.user import created_new_user, get_user, get_users
from app.models.user import User
from app.schemas.user import UserResponse, UserCreated, Userlogin, UserloginResponse
from app.cruds.auth import create_access_token, get_password_hash, check_email, authenticate_user

router = APIRouter()

SessionDp = Annotated[Session, Depends(get_db)]


@router.get('/', status_code=200, response_model=list[UserResponse])
def get_all_user(db: SessionDp, skip: int = 0, limit: int = 10):
    users: list[User] | bool = get_users(db=db, skip=skip, limit=limit)
    if not users:
        raise HTTPException(status_code=404, detail='no registered users')
    return users


@router.get('/{user_id}', status_code=200, response_model=UserResponse)
def get_by_user(db: SessionDp, user_id: int):
    user: User | bool = get_user(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user


@router.post('/', status_code=201, response_model=UserResponse)
def create_user(db: SessionDp, user: UserCreated):
    # hash password generator
    hashed_password = get_password_hash(user.password)
    user.password = hashed_password

    existing_user = check_email(db, user.email)

    if existing_user:
        raise HTTPException(status_code=400, detail='email already registered')

    return created_new_user(db=db, user=user)


@router.post('/login', status_code=200, response_model=UserloginResponse)
def login(db: SessionDp, user: Userlogin):

    existing_user = authenticate_user(
        db=db, email=user.email, password=user.password)

    if not existing_user:
        raise HTTPException(status_code=400, detail='Invalid credentials')
    else:
        access_token = create_access_token(data={'sub': existing_user.name})

        return {"access_token": access_token, "token_type": "bearer"}
