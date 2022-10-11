from pyexpat import model
from fastapi import Depends, APIRouter
from requests import delete
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import models
from pydantic import BaseModel
from typing import Optional
from routers import auth
import sys
sys.path.append('..')


router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={404: {
        'description': 'Not found'
    }}
)

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class UserVerification(BaseModel):
    username: str
    password: str
    new_password: str


@router.get('/')
async def read_all_users(db: Session = Depends(get_db)):
    return db.query(models.Users).all()


@router.get('/user/{user_id}')
async def get_user_by_path(user_id: int, db: Session = Depends(get_db)):
    user_model = db.query(models.Users).filter(
        models.Users.id == user_id).first()
    if user_model is not None:
        return user_model
    return 'Invalid user_id'


@router.get('/user/')
async def user_by_query_param(user_id: int, db: Session = Depends(get_db)):
    user_model = db.query(models.Users).filter(
        models.Users.id == user_id).first()

    if user_model is not None:
        return user_model
    return 'Invalid user_id'


@router.put('/user/password_change')
async def user_password_change(user_verification: UserVerification,
                               user: dict = Depends(auth.get_current_user),
                               db: Session = Depends(get_db)):
    if user is None:
        raise auth.get_user_exception()
    user_model = db.query(models.Users).filter(
        models.Users.id == user.get('id')).first()
    if user_model is not None:
        if user_verification.username == user_model.username and auth.verify_password(
                user_verification.password,
                user_model.hashed_password):
            user_model.hashed_password = auth.get_password_hash(
                user_verification.new_password)
            db.add(user_model)
            db.commit()
            return 'Password update successful'
    return 'Invalid user or request'


@router.delete('/delete_user')
async def delete_user(user: dict = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise auth.get_user_exception()

    user_model = db.query(models.Users).filter(
        models.Users.id == user.get('id')).first()
    if user_model is None:
        return 'Invalid User or Request'

    db.query(models.Users).filter(models.Users.id == user.get('id')).delete()
    db.commit()
    return 'User Deleted Successfully!'
