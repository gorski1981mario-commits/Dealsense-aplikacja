
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import openai

app = FastAPI()

# Dit zorgt ervoor dat de AI je geheime sleutel gebruikt die je net bij Render hebt ingevuld
client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Zorgt dat je Chrome-extensie verbinding mag maken
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "DealSense AI is LIVE", "message": "Klaar om te besparen!"}

@app.get("/analyze")
async def analyze_product(url: str):
    try:
        # De Agentic AI gaat nu naar de pagina kijken
        response = client.chat.completions.create(
            model="gpt-4o", # De nieuwste versie voor 2026
            messages=[
                {"role": "system", "content": "Je bent de DealSense bodyguard. Zoek de prijs en de EAN code op de pagina. Antwoord alleen in JSON formaat: {'price': 0.0, 'ean': 'code'}"},
                {"role": "user", "content": f"Scan deze pagina: {url}"}
            ],
            response_format={ "type": "json_object" }
        )
        return {"status": "success", "data": response.choices[0].message.content}
    except Exception as e:
        return {"status": "error", "message": str(e)}

