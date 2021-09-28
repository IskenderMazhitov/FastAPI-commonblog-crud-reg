from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get('/blog')
def index(published: bool = True, limit=10, sort: Optional[str] = None):
    #only get 10 published blogs
    if published:
        return {
            'data': f'blog list of {limit} published'}
    else:
        return {'data': f"{limit} blogs from the db"}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished block'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int, limit = 10):
    return {'data': {1, 2}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    pass

@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f"Blog is created with title-name: {request.title}"}

# if __name__ == "__main__":
#     uvicorn.run(app, host='127.0.0.1', port=9000)