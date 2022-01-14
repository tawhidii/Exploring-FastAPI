from fastapi import APIRouter, status, Response, Query, Path, Body
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter(prefix='/product', tags=['products'])


class ProductModel(BaseModel):
    title: str
    category_name: str
    price: int
    is_available: bool = True


# create product in inventory
@router.post('/create',
             status_code=status.HTTP_200_OK,
             response_description='Create Product Inventory',
             summary='API endpoint for creating product in Inventory')
def create_product(product: ProductModel, response: Response):
    if product.title.startswith('J'):
        response.status_code = status.HTTP_403_FORBIDDEN
        return {'message': 'Can not entry product name starts with J '}
    return {
        'product': product
    }


# create product by id
@router.post('/new/{id}')
def crete_product_by_id(id: int, product: ProductModel, version: Optional[int] = 0):
    return {
        'id': id,
        'product': product,
        'version': version
    }


class ReviewModel(BaseModel):
    title: str
    content: str


# Review Endpoint
@router.post('/review/{user_id}')
def post_review(
        review: ReviewModel, user_id: int = Path(None, ge=2, le=8, deprecated=True),
        version: str = Query(None, deprecated=True, alias='VERSION'),
        content: str = Body('This is a <Body> content')
):
    return {
        'user_id': user_id,
        'review': review,
        'version': version,
        'content': content
    }
