import ee
import uvicorn
from fastapi import FastAPI

from core.config import EE_SERVICE_ACCOUNT, PRIVATEKEY
from db.base import database
from endpoints.fields import router

app = FastAPI()
app.include_router(router, prefix='/fields', tags=['fields'])


@app.on_event("startup")
async def startup():
    service_account = EE_SERVICE_ACCOUNT
    credentials = ee.ServiceAccountCredentials(
        service_account, PRIVATEKEY)
    ee.Initialize(credentials)
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)
