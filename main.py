import uvicorn
from fastapi import FastAPI

if __name__ == '__main__':
    uvicorn.run(app='core.server:app', port=8000, reload=True, workers=1)
