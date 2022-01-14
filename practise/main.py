from fastapi import FastAPI
from routers import get_products,post_products
app = FastAPI()

app.include_router(get_products.router)
app.include_router(post_products.router)


