from fastapi import FastAPI
from fastapi import File, UploadFile
from pydantic import BaseModel

import os
import time

import database.insert
import database.base
import database.select
import database.delete

app = FastAPI()

@app.get("/")
async def readRoot():
    return {"It's working!"}

@app.post("/upload")
async def file_upload(file: UploadFile, uid: int):
    directory = "D:/testfile"
    if not os.path.exists(directory):
        os.makedirs(directory)
    path = os.path.join(directory, file.filename)
    
    with open(path, "wb") as f:
        content = await file.read()
        f.write(content)
    database.insert.insertFile(uid, file.filename, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    return {"file_size": len(content), "filename": file.filename}

@app.post("/register")
async def register(username: str, password: str, email: str):
    database.base.initDatabase()
    database.insert.insertUser(username, password, email)
    return {"message": "User registered successfully!"}

@app.post("/select/user")
async def select_user(uid: int):
    user = database.select.selectUser(uid)
    return {"user": user}

@app.post("/select/file")
async def select_file(uid: int):
    files = database.select.selectFileByUid(uid, )
    return {"files": files,
            "file_count": len(files)}

@app.post("/delete/user")
async def delete_user(uid: int):
    return {"message": database.delete.deleteUser(uid)}

@app.post("/delete/file")
async def delete_file(file_id: int):
    return {"message": database.delete.deleteFile(file_id)}