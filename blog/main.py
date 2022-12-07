from fastapi import FastAPI
from . import schemas as db

app=FastAPI()
@app.post('/blog')
def create(request:db.Blog):
    return request