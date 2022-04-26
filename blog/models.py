from cgi import print_form
from sqlalchemy import Column, String, Integer
from .database import Base

class Blog(Base):

    __tablename__ = 'blogs'

    id = Column(Integer, index=True, primary_key=True)
    title = Column(String)
    body = Column(String)