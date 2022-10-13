from .auth import get_current_user, get_user_exception
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models
from fastapi import Depends, HTTPException, APIRouter
from typing import Dict, Optional
import sys
sys.path.append('..')

router = APIRouter(
    prefix='/address',
    tags=['address'],
    responses={
        404: {
            'description': 'Not found'
        }
    }
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Address(BaseModel):
    address1: str
    address2: Optional[str]
    city: str
    state: str
    country: str
    postal_code: str


@router.post('/create_address')
async def create_address(address: Address, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()

    address_model = models.Address()
    address_model.address1 = address.address1
    address_model.address2 = address.address2
    address_model.city = address.city
    address_model.state = address.state
    address_model.country = address.country
    address_model.postal_code = address.postal_code

    db.add(address_model)
    db.flush()

    user_model = db.query(models.Users).filter(
        models.Users.id == user.get('id')).first()
    print(f'user model addr_id :{user_model.address_id}')
    user_model.address_id = address_model.id
    print(f'user model ids :{user_model.address_id , address_model.id}')

    # adding the id to user(address_id) column using the id from address model.
    db.add(user_model)
    db.commit()

    return successful_response(201)


# Success Response
def successful_response(statuscode: int):
    return {
        'status': statuscode,
        'transaction': 'Successful'
    }
