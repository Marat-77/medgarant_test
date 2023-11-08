from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

index_router = APIRouter(
    prefix='',
    tags=['Index'],
    responses={404: {'description': 'Not Found'}}
)


@index_router.get('/', status_code=status.HTTP_200_OK)
async def index_page():
    payload = {'message': 'Hello, world!'}
    return JSONResponse(content=payload)
