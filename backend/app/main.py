#Only Skeleton

from fastapi import FastAPI

app = FastAPI(title="Enterprise Knowledge Assistant")

@app.get("/")
def health():
    return {
        "status": "running"
    }