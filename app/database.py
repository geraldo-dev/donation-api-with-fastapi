from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import settings

from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import Depends


engine = create_engine(settings.DATABASE_URL, connect_args={
                       'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    with SessionLocal() as session:
        yield session


SessionDp = Annotated[Session, Depends(get_db)]


def init_db():
    print("Criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
