from sqlalchemy.orm import Session
from app.schemas.user import UserCreated
from passlib.hash import bcrypt
from app.models.user import User


def get_user(db: Session, user_id: int):
    ...


def get_users(db: Session, skip: int = 0, limit: int = 10):
    ...


def check_email(db: Session, email: str):
    # valida se email ja cadastrado
    find_email: User | None = db.query(
        User).filter(User.email == email).first()
    if not find_email:
        return False
    return find_email


def created_user(db: Session, user: UserCreated):
    # geraldo senha hash
    hashed_password = bcrypt.hash(user.password)


def updated_user(db: Session, user: UserCreated):
    ...


def deleted_user(db: Session, user: UserCreated):
    ...
