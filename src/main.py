#!/usr/bin/env python3

from fastapi import FastAPI
from src.routers import books


app = FastAPI(title="Books API")

app.include_router(books.router, prefix="/books", tags=["books"])


@app.get("/")
def read_root():
    return {"message": "Welcome to Books API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
