from fastapi import FastAPI

app = FastAPI()


# get the all products
@app.get('/products/all')
def get_products():
    return {'message': 'All products provided !!'}


# get product by id
@app.get('/product/{product_id}')
def get_by_id(product_id: int):
    return {'message': f'Product ID is {product_id}'}
