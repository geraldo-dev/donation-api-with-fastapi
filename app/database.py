from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'sqlite:///./db.db'

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
Base = declarative_base()
