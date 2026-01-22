
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Kluczowe dla wtyczki Chrome: pozwala na połączenie
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "DealSense Online", "message": "System Bodyguarda gotowy"}

@app.get("/analyze")
async def analyze(url: str, ean: str = "brak"):
    # Tutaj AI Agentic (GPT-4o Vision) będzie analizować cenę
    return {
        "status": "success",
        "ean": ean,
        "recommendation": "CZEKAJ - cena spadnie o 10% w poniedziałek",
        "best_price": 45.99,
        "stripe_url": "https://buy.stripe.com"
    }

if __name__ == "__main__":
    import uvicorn
    # Render wymaga dynamicznego portu
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
