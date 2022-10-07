
from operator import mod
from statistics import mode
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# get DB


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class ToDo(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(
        gt=0, lt=6, description='The Priority must be between 1-5')
    complete: bool


# getting session from get_db() method.

# API - to get all todos table data


@app.get('/')
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()

# get data by todo_id


@app.get('/todo/{todo_id}')
async def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo_model = db.query(models.Todos).filter(
        models.Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise http_exception()


# create todo item
@app.post('/')
async def create_todo(todo: ToDo, db: Session = Depends(get_db)):
    todo_model = models.Todos()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete

    db.add(todo_model)
    db.commit()

    return successful_response(201)


# Update todo item
@app.put('/{todo_id}')
async def update_todo(todo_id: int, todo: ToDo, db: Session = Depends(get_db)):
    todo_model = db.query(models.Todos).filter(
        models.Todos.id == todo_id).first()

    if todo_model is None:
        raise http_exception()

    todo_model.title = todo.title
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete

    db.add(todo_model)
    db.commit()

    return successful_response(200)

# Delete todo Item


@app.delete('/{todo_id}')
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo_model = db.query(models.Todos).filter(
        models.Todos.id == todo_id
    ).first()

    if todo_model is None:
        raise http_exception()

    db.query(models.Todos).filter(models.Todos.id == todo_id).delete()
    db.commit()

    return successful_response(200)

    # Raised HTTP Exception function


# Successful Response


def successful_response(statuscode: int):
    return {
        'status': statuscode,
        'transaction': 'Successful'
    }


def http_exception():
    return HTTPException(status_code=404, detail='Todo not found')
