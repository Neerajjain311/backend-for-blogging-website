from pydantic import BaseModel
from blog.database import Base
from typing import List


class User(BaseModel):
    name: str
    email: str
    password: str


class BaseBlog(BaseModel):
    title: str
    body: str


class Blog(BaseBlog):
    class Config():
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []
    class Config():
        orm_mode = True
        

class ShowBlog(Blog):

    creator: ShowUser
    class Config():
        orm_mode = True
