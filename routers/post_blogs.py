from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict

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


# Custom type
class Image(BaseModel):
    url: str


class CommentModel(BaseModel):
    title: str
    comment_body: str
    is_published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1': 'value2'}
    image: Optional[Image] = None


# Example of Parameter metadata with validators
@router.post('/new/{id}/comment')
def create_comment(comment: CommentModel,
                   id: int,
                   comment_title: int = Query(None,
                                              alias='commentId',
                                              deprecated=True),
                   comment_id: int = Path(None, ge=3, le=5),
                   content=Body(...),
                   versions: Optional[List[str]] = Query(['1.0', '1.1'])
                   ):
    return {
        'id': id,
        'comment': comment,
        'comment_id': comment_id,
        'content_id': content,
        'versions': versions,
        'comment_title': comment_title
    }
