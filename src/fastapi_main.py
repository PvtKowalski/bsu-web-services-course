from fastapi import FastAPI
import asyncio
import multiprocessing
import threading


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/sleep')
async def asgi_sleep():
    print(
        multiprocessing.current_process().name,
        threading.current_thread().name
    )
    await asyncio.sleep(2)
    return {"concurrency": "and stuff???"}
