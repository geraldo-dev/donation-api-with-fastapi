from typing import Annotated
from sqlalchemy import create_engine, Session
from fastapi import Depends
from sqlalchemy.orm import declarative_base
from app.config import settings


engine = create_engine(settings.DATABASE_URL, connect_args={
                       'check_same_thread': False})
Base = declarative_base()


def get_db():
    with Session(engine) as session:
        yield session


SessionDp = Annotated[Session, Depends(get_db)]


def init_db():
    print("Criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
