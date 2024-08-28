from fastapi import FastAPI, WebSocket
from typing import List

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app!, hot reload works"}
