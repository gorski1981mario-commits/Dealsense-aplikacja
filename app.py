from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # Dit is HTML-code direct in je Python-bestand
    html_content = """
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dealsen Aplikacja</title>
        <link href="cdn.jsdelivr.net" rel="stylesheet">
    </head>
    <body class="bg-light">
        <div class="container mt-5">
            <div class="card shadow">
                <div class="card-body text-center">
                    <h1 class="card-title text-primary">Witaj w Dealsen Aplikacja!</h1>
                    <p class="card-text">Twoja aplikacja Python działa i wygląda profesjonalnie.</p>
                    <hr>
                    <p>Dzisiejsza data: <strong>11 januari 2026</strong></p>
                    <button class="btn btn-success" onclick="alert('Działa!')">Testuj funkcję</button>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

