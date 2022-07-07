from fastapi import FastAPI

from shortener.db import database
from shortener.routes import router

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def on_startup() -> None:
    await database.connect()   
   

@app.on_event("shutdown")
async def on_shutdown() -> None:
    await database.disconnect()   
