from fastapi import FastAPI, UploadFile, HTTPException, Depends
from pydantic import BaseModel
import jwt
import os
import time

import database.insert
import database.base
import database.select
import database.delete
import security.security
import globalVariables

app = FastAPI()

@app.get("/")
async def readRoot():
    return {"It's working!"}

@app.post("/upload")
async def file_upload(file: UploadFile, uid: int):
    if not os.path.exists(globalVariables.directory):
        os.makedirs(globalVariables.directory)
    path = os.path.join(globalVariables.directory, file.filename)
    
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
    user = database.select.selectUserByUid(uid)
    return {"user": user}

@app.post("/select/file")
async def select_file(uid: int):
    files = database.select.selectFileByUid(uid)
    return {"files": files, "file_count": len(files)}

@app.post("/delete/user")
async def delete_user(uid: int):
    return {"message": database.delete.deleteUser(uid)}

@app.post("/delete/file")
async def delete_file(file_id: int):
    return {"message": database.delete.deleteFile(file_id)}

class Token(BaseModel):
    access_token: str
    token_type: str

@app.post("/login", response_model = Token)
async def login(username: str, password: str):
    user = database.select.selectUserByUsername(username)
    if user == "User not found!":
        raise HTTPException(status_code=404, detail="User not found!")
    if user[2] != password:
        raise HTTPException(status_code=401, detail="Password is incorrect!")
    access_token = security.security.create_access_token(data={"sub": user[0]})
    return {"access_token": access_token, "token_type": "bearer"}

async def get_current_user(token: str = Depends(security.security.oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, security.security.SECURITY_KEY, algorithms=[security.security.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception
    user = database.select.selectUserByUsername(username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: dict = Depends(get_current_user)):
    if current_user["disabled"]:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user