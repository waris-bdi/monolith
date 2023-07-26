from fastapi import FastAPI, HTTPException, Header

app = FastAPI()

mocked_movies_data = [
    {"id": 1, "name": "Movie 1", "genre": "Action"},
    {"id": 2, "name": "Movie 2", "genre": "Adventure"},
]


@app.get("/movies/")
async def read_movies(x_api_key: str = Header()):
    if x_api_key:
        success = authen(x_api_key)
        if success:
            return {"data": mocked_movies_data}
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")
    else:
        raise HTTPException(status_code=400, detail="No API key provided")


mocked_books_data = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
]


@app.get("/books/")
async def read_books(x_api_key: str = Header()):
    if x_api_key:
        success = authen(x_api_key)
        if success:
            return {"data": mocked_books_data}
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")
    else:
        raise HTTPException(status_code=400, detail="No API key provided")


def authen(x_api_key: str):
    if not x_api_key:
        raise HTTPException(status_code=400, detail="x_api_key header missing")

    if x_api_key == "thisiscool":
        return {"authorized": True}

    raise HTTPException(status_code=401, detail="Unauthorized")
