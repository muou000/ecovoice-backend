from fastapi import FastAPI
from fastapi import File, UploadFile
import os
app = FastAPI()

@app.get("/")
async def readRoot():
    return {"It's working!"}

@app.post("/upload")
async def file_upload(file: UploadFile):
    directory = "D:/testfile"
    if not os.path.exists(directory):
        os.makedirs(directory)
    path = os.path.join(directory, file.filename)
    
    with open(path, "wb") as f:
        content = await file.read()
        f.write(content)
    return {"file_size": len(content), "filename": file.filename}
    