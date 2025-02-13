from fastapi import FastAPI
from .database import init_db
from app.routes import user

app: FastAPI = FastAPI(
    title='donation-api-with-fastapi',
    description='donation api so that anyone can donate and register who did',
    version='1.1.0'
)

app.include_router(user.router, prefix='/users', tags=['users'])


@app.get('/')
def read_root():
    return {'message': 'welcome too be Api'}


if __name__ == "__main__":
    init_db()
