from typing import Optional

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from medgarant_fastapi_test.services import DoctorTime

get_times_router = APIRouter(
    prefix='/times',
    tags=['DoctorTime'],
    responses={404: {'description': 'Not Found'}}
)


@get_times_router.get('/', status_code=status.HTTP_200_OK)
async def get_times(minutes: Optional[int] = None):
    doc_time = DoctorTime()
    if minutes:
        payload = doc_time.get_free_times(minutes)
        return JSONResponse(content=payload)
    payload = doc_time.get_free_times()
    return JSONResponse(content=payload)


