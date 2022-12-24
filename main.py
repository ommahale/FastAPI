from fastapi import FastAPI,File,UploadFile
from typing import Optional
from pydantic import BaseModel


class Blog(BaseModel):
    id: int
    data: str


app=FastAPI()
userInfo={'data':[
        {
            'userID':1,
            'name':'Om'
        },
        {
            'userID':2,
            'name':'Yash'
        },
        {
            'userID':3,
            'name':'Kundan'
        }
    ]}

@app.get('/showdb')
def pub(limit=10,pub:bool=True,sort:Optional[str]=None):
    if(pub):
        return {'data':f'returned {limit} books that are published'}
    else:
        return {'data':f'returned {limit} books that are not published'}

@app.get('/{id}')
def show(id:int):
    if(id>0 and id<len(userInfo['data'])+1):
        return userInfo['data'][id-1]
    else:
        return {'error':'out of index'}

@app.get('/')
def index():
    return userInfo

@app.post('/blog')
def blog(blog: Blog):
    return {'data':blog}

# if __name__=='__main__':
#     uvicorn.run(app,host='127.0.0.1',port=9000)

@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}