from enum import unique
from pyparsing import empty
from sqlalchemy import Column, String, Integer, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Blog(Base):

    __tablename__ = 'blogs'

    id = Column(Integer, index=True, primary_key=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship('User', back_populates= 'blogs')

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, index=True, primary_key= True)
    name = Column(String)
    email = Column(String, unique= True)
    password = Column(String)

    blogs = relationship('Blog', back_populates = 'creator')
