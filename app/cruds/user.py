from sqlalchemy.orm import Session
from app.schemas.user import UserCreated
from passlib.hash import bcrypt
from app.models.user import User


def get_user(db: Session, user_id: int):
    find_user = db.query(
        User).filter(User.id == user_id).first()

    if not find_user:
        return False
    return find_user


def get_users(db: Session, skip: int = 0, limit: int = 10):
    ...


def check_email(db: Session, email: str):

    find_email = db.query(
        User).filter(User.email == email).first()

    if not find_email:
        return False
    return find_email


def created_new_user(db: Session, user: UserCreated):
    # hash password generator
    hashed_password = bcrypt.hash(user.password)

    new_user = User(
        name=user.name,
        email=user.email,
        age=user.age,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def updated_user(db: Session, user: UserCreated):
    ...


def deleted_user(db: Session, user: UserCreated):
    ...
