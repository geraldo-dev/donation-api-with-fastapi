from sqlalchemy.orm import Session
from app.schemas.user import UserCreated
from app.models.user import User


def get_user(db: Session, user_id: int):
    user = db.query(
        User).filter(User.id == user_id).first()

    if not user:
        return False
    return user


def get_users(db: Session, skip: int, limit: int) -> list[User] | bool:
    users = db.query(User).offset(skip).limit(limit).all()

    if not users:
        return False
    return users


def created_new_user(db: Session, user: UserCreated):
    new_user = User(
        name=user.name,
        email=user.email,
        age=user.age,
        hashed_password=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def updated_user(db: Session, user: UserCreated):
    ...


def deleted_user(db: Session, user: UserCreated):
    ...
