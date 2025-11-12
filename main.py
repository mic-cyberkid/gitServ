# server.py
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000, log_level="info")
