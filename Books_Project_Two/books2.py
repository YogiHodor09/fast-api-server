from typing import Optional
from uuid import UUID

from fastapi import FastAPI, HTTPException, Request, status, Form, Header
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse


# Negative number exception

class NegativeNumberException(Exception):
    def __init__(self, book_to_return):
        self.books_to_return = book_to_return


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


class BookNoRating(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title='Description of the book', max_length=100, min_length=1)


BOOKS = []


# Custom Exception Handler decorator

@app.exception_handler(NegativeNumberException)
async def negative_number_exception_handler(request: Request, exception: NegativeNumberException):
    return JSONResponse(
        status_code=418,
        content={'message': f'Hey , Why you need {exception.books_to_return} books? You need to read more!'},
    )


# Created login for books page
@app.post('/books/login')
async def books_login(username: str = Form(), password: str = Form()):
    return {'username': username, 'password': password}


# Create Random Header in Request
@app.get('/header')
async def read_header(random_header: Optional[str] = Header(None)):
    return {'Random-Header': random_header}


# Read all books if optional book number not give or
# given as per requirement how many books wants to return
@app.get('/')
async def read_all_books(book_to_return: Optional[int] = None):
    if book_to_return and book_to_return < 0:
        raise NegativeNumberException(book_to_return=book_to_return)

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
    raise raise_item_cannot_be_found_exception()


# Response Model with no_rating customised
@app.get('/book/rating/{book_id}', response_model=BookNoRating)
async def read_book_no_rating(book_id: UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x
    raise raise_item_cannot_be_found_exception()


@app.post('/',
          status_code=status.HTTP_201_CREATED)  # Created custom response code HTTP_201_CREATED for success response
async def create_book(book: Book):
    BOOKS.append(book)
    return book


# Update book by UUID
@app.put('/{book_id}')
async def update_book(book_id: UUID, book: Book):
    counter = 0

    for x in BOOKS:
        counter += 1
        print(f'counter update value : {counter}')
        if x.id == book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]
    raise raise_item_cannot_be_found_exception()


@app.delete('/{book_id}')
async def delete_book(book_id: UUID):
    counter = 0
    for x in BOOKS:
        counter += 1
        print(f'counter delete value : {counter}')
        if x.id == book_id:
            del BOOKS[counter - 1]
            return f'ID: {book_id} deleted'

    raise raise_item_cannot_be_found_exception()


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


def raise_item_cannot_be_found_exception():
    return HTTPException(status_code=404, detail='Book not found!',
                         headers={'X-Header-Error': 'Nothing to be seen at UUID'})
