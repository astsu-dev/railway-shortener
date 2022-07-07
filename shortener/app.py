import os
import uvicorn
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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ["PORT"]))
