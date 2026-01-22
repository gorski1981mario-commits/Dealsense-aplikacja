
from fastapi import FastAPI

app = FastAPI(title="Dealsense API", version="0.1")

@app.get("/")
def healthcheck():
    return {
        "status": "ok",
        "service": "dealsense-backend"
    }
