from fastapi import FastAPI
from database import init_db

app: FastAPI = FastAPI(
    title='donation-api-with-fastapi',
    description='donation api so that anyone can donate and register who did',
    version='1.1.0'
)

if __name__ == "__main__":
    init_db()
