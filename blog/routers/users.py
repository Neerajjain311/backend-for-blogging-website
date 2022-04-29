import imp
from fastapi import APIRouter, status, Depends, HTTPException
from ..hashing import Hash
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repository import users


router = APIRouter(
    prefix='/users',
    tags=['Users']
)

# GET Specific user details
@router.get('/{id}', status_code= status.HTTP_200_OK, response_model= schemas.ShowUser)
def get_user_by_id(id: int, db: Session = Depends(database.get_db)):
    return users.get_user(id, db)


# Create New User
@router.post('/', response_model=schemas.ShowUser, status_code= status.HTTP_201_CREATED)
def create_user(user: schemas.User, db: Session = Depends(database.get_db)):
    return users.create_new_user(user, db)