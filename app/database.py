from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///./db.db', echo=True)
SessionLocal: sessionmaker[Session] = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    print("Criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
