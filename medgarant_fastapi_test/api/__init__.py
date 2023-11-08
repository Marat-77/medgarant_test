from fastapi import FastAPI

from .v_1.get_times_router import get_times_router
from .v_1.index_router import index_router

app = FastAPI()
# app.include_router(user_router)
app.include_router(index_router)
app.include_router(get_times_router)
