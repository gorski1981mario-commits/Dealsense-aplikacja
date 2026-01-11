from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Dealsen Aplikacja draait succesvol op Render!"

if __name__ == "__main__":
    # Gebruik de poort die Render toewijst
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
