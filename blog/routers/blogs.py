from fastapi import APIRouter, status, Depends
from typing import List
from .. import schemas, database, oauth2
from sqlalchemy.orm import Session
from ..repository import blogs

router = APIRouter(
    prefix='/blogs',
    tags= ['Blogs']
)

# Method to create new blog
@router.post('/', status_code= status.HTTP_201_CREATED)
def create_new_blog(blog: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogs.create_blog(blog, db)


# Get all  blogs
@router.get('/', response_model= List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogs.show_all(db)


# Get particular blog based on ID
@router.get('/{id}', status_code= status.HTTP_200_OK, response_model= schemas.ShowBlog)
def get_blog_by_id(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogs.get_by_id(id, db)
    

# DELETE particular blog based on ID
@router.delete('/{id}', status_code= status.HTTP_204_NO_CONTENT)
def delete_blog_by_id(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogs.destroy(id, db)


# UPDATE particular blog
@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogs.update(id, request, db)