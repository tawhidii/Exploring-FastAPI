from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()


@app.get('/')
def index():
    json_message = {'message': 'Hello world !!'}
    return json_message


# *** Ordering ***
@app.get('/blog/all')
def get_all_blog():
    return {'message': 'Provided all blog !!'}


# Example of pre-defined path
# For specific path value we will use Enum of python
class BlogType(str, Enum):
    short = 'short_type'
    long = 'long_type'
    howto = 'howto_type'


@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    if BlogType.howto == 'howto_type':
        print('It is working !!')
    return {'message': f'Blog type is {type}'}


# Example of path parameter
@app.get('/blog/{id}')
def get_blog_post(id: int):  # pydentic : type validation
    return {'message': f'Blog with id {id}'}


# Example of Query Parameter

@app.get('/comments/all')
def show_comments(page=1, page_size: Optional[int] = None):
    return {'message': f'All {page_size} comments on page {page}'}


# Example combine of Query And Path parameter
@app.get('/comment/{id}/of/{comment_id}/')
def get_comment(id: int, comment_id: int, is_valid: bool = True, username: Optional[str] = None):
    return {'message': f'From {id} of comment id {comment_id} username is {username} ,  is Valid {is_valid}'}
