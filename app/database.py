from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


DATABASE_URL = 'sqlite:///./db.db'

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
Base = DeclarativeBase()
