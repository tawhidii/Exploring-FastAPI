from fastapi import APIRouter
from enum import Enum

router = APIRouter(prefix='/blog', tags=['blog'])


@router.get('/all')
def get_all_blog():
    return {'message': 'Provided all blog !!'}


class BlogType(str, Enum):
    short = 'short_type'
    long = 'long_type'
    howto = 'howto_type'


@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    if BlogType.howto == 'howto_type':
        print('It is working !!')
    return {'message': f'Blog type is {type}'}


@router.get('/{id}')
def get_blog_post(id: int):  # pydentic : type validation
    return {'message': f'Blog with id {id}'}
