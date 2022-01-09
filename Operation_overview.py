from fastapi import FastAPI, status, Response
from typing import Optional

app = FastAPI()


# Example of Status Code
@app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blog'])
def get_blogs(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found !!'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with ID : {id}'}


# Example of tags and use docstring as a description
@app.get('/comment/{id}/of/{comment_id}/', tags=['comment'])
def get_comment(id: int, comment_id: int, is_valid: bool = True, username: Optional[str] = None):
    """
    Getting comments with id and comment id.
    - **id** : required
    - **comment_id**: required
    - **is_valid**: required
    - **username**: Optional
    """
    return {'message': f'From {id} of comment id {comment_id} username is {username} ,  is Valid {is_valid}'}


# Example of summery and description
@app.get('/posts/all',
         tags=['post'],
         summary='Get all the post',
         description='This api endpoint will provide all the post which is published',
         response_description='List of all available post')
def get_posts():
    return {'message': 'All posts provided!!'}
