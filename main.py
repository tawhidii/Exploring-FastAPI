from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    json_message = {'message': 'Hello world !!'}
    return json_message


# *** Ordering ***
@app.get('/blog/all')
def get_all_blog():
    return {'message':'Provided all blog !!'}

# Example of path parameter
@app.get('/blog/{id}')
def get_blog_post(id:int): # pydentic : type validation
    return {'message': f'Blog with id {id}'}


