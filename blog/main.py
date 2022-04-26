from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Method to create new blog
@app.post('/blogs', status_code= status.HTTP_201_CREATED)
def create_new_blog(blog: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title= blog.title, body= blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# Get all blogs
@app.get('/blogs')
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


# Get particular blog based on ID
@app.get('/blogs/{id}', status_code= status.HTTP_200_OK)
def get_blog_by_id(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'Blog with id {id} not available!')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message' : f'Blog with id {id} not available!'}
    return blog 

