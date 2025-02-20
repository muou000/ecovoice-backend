import uvicorn
from fastapi import FastAPI
import core.server

if __name__ == '__main__':
    uvicorn.run(app='core.server:app', host='0.0.0.0', port=8000, reload=True, workers=1)
