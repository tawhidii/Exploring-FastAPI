from fastapi import FastAPI
from routers import get_blogs
app = FastAPI()

app.include_router(get_blogs.router)