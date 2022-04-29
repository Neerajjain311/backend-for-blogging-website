import imp
from fastapi import Depends, HTTPException, status
from .. import models, database, schemas, hashing
from sqlalchemy.orm import Session

def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'User with id {id} not available!')
       
    return user


def create_new_user(user: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(name= user.name, email= user.email, password= hashing.Hash.bcrypt(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user