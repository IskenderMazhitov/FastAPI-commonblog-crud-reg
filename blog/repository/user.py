from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas
from .. import hashing

def create(db: Session, request: schemas.User):
    new_user = models.User(username=request.username, email=request.email,
                           age=request.age, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with such {id} id ain't found")
    return user

def get_all(db: Session):
    list_of_users = db.query(models.User).all()
    return list_of_users
