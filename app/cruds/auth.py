from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from passlib.hash import bcrypt
from app.models.user import User
from app.config import settings

# refatora
from typing import Annotated
from fastapi import Depends, HTTPException
from app.database import get_db
SessionDp = Annotated[Session, Depends(get_db)]


def check_email(db: Session, email: str):

    find_email = db.query(
        User).filter(User.email == email).first()

    if not find_email:
        return False
    return find_email


def get_password_hash(password: str):
    return bcrypt.hash(password)


def verify_password(plain_password, hashed_password):
    return bcrypt.verify(plain_password, hashed_password)


def authenticate_user(db: Session, email: str, password: str):

    user = check_email(db, email)

    if not user or not verify_password(password, user.hashed_password):
        return False

    return user


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def get_current_user(token: str, db: SessionDp):
    creadentials_exception = HTTPException(
        status_code=401, detail="Invalid token")
    try:
        payload = jwt.decode(token, settings.SECRET_KEY,
                             algorithms=[settings.ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise creadentials_exception
    except JWTError:
        raise creadentials_exception

    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise creadentials_exception
    return user
