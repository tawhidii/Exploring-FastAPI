from fastapi import APIRouter, Response, status

router = APIRouter(prefix='/product', tags=['products'])


# get the all products
@router.get('/all',)
def get_products():
    return {'message': 'All products provided !!'}


# get product by id
@router.get(
    '/{product_id}',
    status_code=status.HTTP_200_OK,
    summary='API endpoint for product by Id',
    description='In this api end point you will get product by passing its id',
    response_description='Product with Id')
def get_by_id(product_id: int, response: Response):
    if product_id > 200:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Product ID is {product_id}'}
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'message': 'Product Not found !!'}
