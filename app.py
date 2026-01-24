
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai

app = FastAPI()

# Zmień tutaj, jeśli chcesz używać innej zmiennej środowiskowej dla klucza OpenAI
client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Zapewnia, że rozszerzenie Chrome może się połączyć (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model Pydantic do przyjmowania danych POST od rozszerzenia
class ProductData(BaseModel):
    current_price: float
    ean: str
    url: str # Adres strony, z której pochodzą dane
    user_id: str # Unikalne ID użytkownika (musisz je dodać w rozszerzeniu)

# Prosta baza danych w pamięci (w MVP możesz użyć np. Redis lub SQLite)
# Przechowujemy liczbę użyć na użytkownika
user_usage = {} 

@app.get("/")
def home():
    return {"status": "DealSense AI is LIVE", "message": "Klaar om te besparen!"}

@app.post("/analyze")
async def analyze_product(data: ProductData):
    # Logika licznika użyć
    if data.user_id not in user_usage:
        user_usage[data.user_id] = 0
    
    # Symulacja: AI znajduje lepszą cenę. W rzeczywistości użyjesz tutaj API Google Shopping lub innej porównywarki.
    # Użyjemy OpenAI Vision/EAN matching tutaj, ale na potrzeby logiki MVP:
    # Załóżmy, że AI znajduje cenę 59.95 EUR
    found_price = 59.95 

    # Logika porównania cen (naprawiona!)
    if found_price < data.current_price:
        savings = round(data.current_price - found_price, 2)
        unlock_fee = round(savings * 0.10, 2)

        if user_usage[data.user_id] >= 3:
            # Użytkownik zablokowany, musi zapłacić 10%
            return {
                "status": "locked", 
                "savings": savings, 
                "unlock_fee": unlock_fee,
                "message": f"Aby zobaczyc oferte, zaplac €{unlock_fee}"
            }
        else:
            # Użytkownik ma darmowe użycie, zwracamy link (Symulacja linku)
            user_usage[data.user_id] += 1
            return {
                "status": "unlocked",
                "savings": savings,
                "found_url": "https://link-do-tanszego-sklepu.com",
                "remaining_spins": 3 - user_usage[data.user_id]
            }
    else:
        # Nie znaleziono tańszej oferty, brak oszczędności
        return {
            "status": "no_deal",
            "message": "Niestety, na bol.com jest aktualnie najlepsza oferta."
        }

