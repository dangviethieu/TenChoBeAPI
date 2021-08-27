from fetch_data import get_first_names, get_names, get_detail
from fastapi import FastAPI

app = FastAPI()

@app.get('/first_names')
async def first_names():
    return get_first_names()

@app.get('/names')
async def names(page: int = 0, limit: int = 10):
    return get_names()[page * limit : (page+1) * limit]

@app.get('/detail')
async def detail(full_name: str):
    return get_detail(full_name.replace(" ", "-"))
