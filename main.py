from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# basepath - '/'
# operation - get
@app.get('/')
def index(limit=10, published: Optional[bool] = True):
    return {'message':f'{limit} {published} Hello World!'}

@app.get('/blogs/{id}')
def get_blog(id: int):
    return {'blog':id}