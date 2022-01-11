from fastapi import APIRouter, Query, Body
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix='/blog', tags=['blog'])

"""Example of request body with pydantic BaseModel
 with path parameter and query parameter"""


class BlogModel(BaseModel):
    title: str
    content: str
    comment_id: int
    is_published: Optional[bool]


@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 2):  # with path and query parameter
    """ Endpoint for create blog post."""
    # will convert to automatic JSON
    print(blog.title)
    return {
        'id': id,
        'data': blog,
        'version': version
    }


class CommentModel(BaseModel):
    title: str
    comment_body: str


# Example of Parameter meta data with validators
@router.post('/new/{id}/comment')
def create_comment(comment: CommentModel,
                   id: int,
                   comment_id: int = Query(None,
                                           alias='commentId',
                                           deprecated=True),
                   content=Body(...,min_length=10,max_length=100)
                   ):
    return {
        'id': id,
        'comment': comment,
        'comment_id': comment_id,
        'content_id': content
    }
