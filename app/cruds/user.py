from sqlalchemy.orm import Session
from app.schemas.user import UserCreated
from passlib.hash import bcrypt


def get_user(db: Session, user_id: int):
    ...


def get_users(db: Session, skip: int = 0, limit: int = 10):
    ...


def created_user(db: Session, user: UserCreated):
    ...


def updated_user(db: Session, user: UserCreated):
    ...


def deleted_user(db: Session, user: UserCreated):
    ...
