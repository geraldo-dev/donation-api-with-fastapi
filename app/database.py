from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from typing import AsyncGenerator

engine = create_async_engine('sqlite:///./db.db', echo=True)

SessionLocal = async_sessionmaker(expire_on_commit=False,
                                  class_=AsyncSession, bind=engine)
Base = declarative_base()


async def get_db() -> AsyncGenerator[AsyncSession | None]:
    async with SessionLocal() as session:
        yield session


def init_db():
    print("Criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
