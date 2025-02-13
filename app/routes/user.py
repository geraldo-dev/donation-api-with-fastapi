from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from typing import Annotated
from app.cruds.user import check_email, created_new_user
from app.models.user import User
from app.schemas.user import UserResponse, UserCreated

router = APIRouter()

# SessionDp = Annotated[Session, Depends(get_db)]


@router.post('/users', status_code=201, response_model=UserResponse)
def create_user(user: UserCreated, db: Session = Depends(get_db)):

    existing_user = check_email(db, user.email)
    print('-----', existing_user)

    if existing_user:
        raise HTTPException(status_code=400, detail='email already registered')

    return created_new_user(db=db, user=user)
