from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    json_message = {'message': 'Hello world !!'}
    return json_message
