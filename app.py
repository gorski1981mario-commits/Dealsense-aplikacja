
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS – poprawnie dla FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

# model danych
class AnalyzeRequest(BaseModel):
    price: float
    ean: str | None = None

@app.post("/analyze")
def analyze(data: AnalyzeRequest):
    return {
        "received_price": data.price,
        "ean": data.ean,
        "message": "Analyze endpoint działa"
    }
