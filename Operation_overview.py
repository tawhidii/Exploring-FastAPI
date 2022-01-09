from fastapi import FastAPI,status,Response

app = FastAPI()


@app.get('/blog/{id}',status_code=status.HTTP_200_OK)
def get_blogs(id: int,response:Response):
    """ Example of Status Code """
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found !!'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with ID : {id}'}
