from app.database import SessionDp
from app.schemas.user import UserResponse, UserCreated


def get_user(db: SessionDp, user_id: int):
    ...


def get_users(db: SessionDp, skip: int = 0, limit: int = 10):
    ...


def created_user(db: SessionDp, user: UserCreated):
    ...


def updated_user(db: SessionDp, user: UserCreated):
    ...


def deleted_user(db: SessionDp, user: UserCreated):
    ...
