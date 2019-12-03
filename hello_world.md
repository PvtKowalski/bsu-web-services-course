# Hello World

## Technologies :thinking:

I was looking for something relatively fast in python, so I went to check [the benchmarks](https://www.techempower.com/benchmarks/). And discovered that the fastest frameworks belong to ASGI, a standard for compatibility between web servers, frameworks, and applications that use asyncronous python.

> An ASGI server is responsible for receiving data as raw bytes and interpreting the bytes in terms of the HTTP or Websocket protocol. Once it has done so it can then send this information to the ASGI Framework.
Currently there are three ASGI servers, Hypercorn, Uvicorn, and Daphne. These mostly differ in the choice of HTTP/Websocket parser.

### (Nginx) + Uvicorn/Gunicorn + (FastAPI) ???

`uvicorn hello:app --reload --port 5000`

`uvicorn fastapi_main:app --reload --port 5000`

`gunicorn -w 4 --bind 127.0.0.1:5000 -k uvicorn.workers.UvicornH11Worker fastapi_main:app`

> Using Nginx as a proxy in front of your Uvicorn processes may not be neccessary, but is recommended for additional resiliance. Nginx can deal with serving your static media and buffering slow requests, leaving your application servers free from load as much as possible.

### Uvicorn/gunicorn + blacksheep ???

### Try other ASGI servers / frameworks combinations ?
