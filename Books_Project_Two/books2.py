from typing import Optional
from uuid import UUID

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book(BaseModel):
    # Using Basemodel to create class objs
    id: UUID  # Universal Unique Identifier
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title='Description of the book', max_length=100, min_length=1)
    rating: int = Field(gt=-1, le=101)

    class Config:
        # Creating pre-defined request-body for Swagger doc.
        schema_extra = {
            'example': {
                'id': '15d347cf-43a9-4b93-86c8-8c9dd550363a',
                'title': 'Computer Science Pro',
                'author': 'Yogeshwar Panneerselvam',
                'description': 'Very Nice Description of the book!',
                'rating': 75
            }
        }


BOOKS = []


# Read all books if optional book number not give or
# given as per requirement how many books wants to return
@app.get('/')
async def read_all_books(book_to_return: Optional[int] = None):
    if len(BOOKS) < 1:
        create_books_no_api()

    if book_to_return and len(BOOKS) >= book_to_return > 0:
        i = 1
        new_books = []
        while i <= book_to_return:
            new_books.append(BOOKS[i - 1])
            i += 1
        return new_books

    return BOOKS


# Read book by UUID
@app.get('/book/{book_id}')
async def read_book(book_id: UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x


@app.post('/')
async def create_book(book: Book):
    BOOKS.append(book)
    return book


# Update book by UUID
@app.put('/{book_id}')
async def update_book(book_id: UUID, book: Book):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]


@app.delete('/{book_id}')
async def delete_book(book_id: UUID):
    counter = 0
    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            del BOOKS[counter - 1]
            return f'ID: {book_id} deleted'


# Create books list for dummy data to list books initially.
def create_books_no_api():
    book_1 = Book(id='b5d347cf-43a9-4b93-86c8-8c9dd550363a', title='Title 1', author='Author 1',
                  description='Description 1', rating=60)
    book_2 = Book(id='c5d347cf-43a9-4b93-86c8-8c9dd550363a', title='Title 2', author='Author 2',
                  description='Description 2', rating=70)
    book_3 = Book(id='d5d347cf-43a9-4b93-86c8-8c9dd550363a', title='Title 3', author='Author 3',
                  description='Description 3', rating=80)
    book_4 = Book(id='e5d347cf-43a9-4b93-86c8-8c9dd550363a', title='Title 4', author='Author 4',
                  description='Description 4', rating=90)

    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)
