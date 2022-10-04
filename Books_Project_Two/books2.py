from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID

app = FastAPI()


class Book(BaseModel):
    # Using Basemodel to create class objs
    id: UUID  # Universal Unique Identifier
    title: str
    author: str
    description: str
    rating: int


BOOKS = []


@app.get('/')
async def read_all_books():
    return BOOKS


@app.post('/')
async def create_book(book: Book):
    BOOKS.append(book)
    return book
