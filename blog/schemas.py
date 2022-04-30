from pydantic import BaseModel
from typing import List, Optional

from blog.database import Base


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
        

class ShowBLogCreator(BaseModel):
    name: str
    email: str
    class Config():
        orm_mode = True
        

class ShowBlog(Blog):

    creator: ShowBLogCreator
    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None