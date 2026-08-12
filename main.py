import uvicorn
from fastapi import FastAPI,Depends
from app.routes.router import router

app = FastAPI()

app.include_router(router, prefix="/api/v1")

@app.get("/health")
def health():
    return {"health": "OK"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)