""" FastAPI application entrypoint. """
import os

import uvicorn
from fastapi import FastAPI
from routes.image import router

api_port = int(os.environ.get("API_PORT", "8000"))

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Python Geospatial Image Processing API"}

app.include_router(router, prefix="/image", tags=["Image"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=api_port)
