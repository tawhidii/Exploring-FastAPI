from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix='/blog', tags=['blog'])


# Example of request body with pydantic BaseModel
class BlogModel(BaseModel):
    title: str
    content: str
    comment_id:int
    is_published: Optional[bool]


@router.post('/new')
def create_blog(blog: BlogModel):
    """ Endpoint for create blog post."""
    # will convert to automatic JSON
    print(blog.title)
    return {'data': blog}
