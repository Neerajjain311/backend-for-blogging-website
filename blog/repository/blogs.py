from .. import schemas, models, database
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session


def create_blog(blog: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title= blog.title, body= blog.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def show_all(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


def get_by_id(id:int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Blog with id {id} not available!')

    return blog 


def destroy(id:int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Blog with id {id} not available!')

    blog.delete(synchronize_session= False)
    db.commit()
    return {'message' : f'Blog with id {id} deleted!'}


def update(id:int ,request: schemas.Blog, db: Session = Depends(database.get_db)):    
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,  detail= f'Blog with id {id} not available!')

    blog.update(request.dict())
    db.commit()
    return {'message' : f'Blog with id {id} updated!'}

