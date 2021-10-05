import re
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, main, models, database
from typing import List
from .. import hashing
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser,)
def create_user(request: schemas.User, db: Session = Depends(database.get_db),):
    return user.create(db, request)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser,)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return user.get(id, db)


@router.get('/', status_code=status.HTTP_200_OK, )
def list_users(db: Session = Depends(database.get_db)):
    return user.get_all(db)
