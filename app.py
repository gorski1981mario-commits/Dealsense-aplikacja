from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # To pozwala wtyczce Chrome łączyć się z tym serwerem

@app.route('/')
def home():
    return "Serwer Dealsense działa i czeka na dane z wtyczki!"

@app.route('/analyze', methods=['POST'])
def analyze():
    # Serwer odbiera dane o produkcie
    data = request.json
    price = data.get('price', 0)
    
    # Symulacja AI Dealsense:
    # W przyszłości tu będzie prawdziwe porównywanie cen
    best_price = float(price) * 0.95  # Symulacja znalezienia ceny o 5% niższej
    savings = float(price) - best_price
    commission = savings * 0.10  # Twoja prowizja (10% od oszczędności)
    
    return jsonify({
        "verdict": "KUPUJ", 
        "reason": "Znaleźliśmy ofertę o 5% tańszą w innym sklepie.",
        "savings_info": f"Oszczędzasz: {round(savings, 2)} EUR",
        "our_fee": f"Nasza prowizja: {round(commission, 2)} EUR"
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
