from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace these with your real Alpaca paper keys
ALPACA_KEY_ID = 'PKSOB352J0MW1TOIECD6'
ALPACA_SECRET_KEY = 'hujr7cgZERs0NYSCzHYBvF5sHDEQxXFJK872UC4y'

@app.route('/alpaca/account', methods=['GET'])
def proxy_account():
    _ = request.headers.get("X-API-KEY")  # Dummy for ChatGPT auth

    headers = {
        'APCA-API-KEY-ID': ALPACA_KEY_ID,
        'APCA-API-SECRET-KEY': ALPACA_SECRET_KEY
    }

    response = requests.get('https://paper-api.alpaca.markets/v2/account', headers=headers)

    if response.status_code != 200:
        return jsonify({"error": "Failed to retrieve account"}), response.status_code

    data = response.json()

    # Cast numeric strings to actual float types for compatibility with ChatGPT
    cleaned = {
        "account_number": data.get("account_number"),
        "status": data.get("status"),
        "currency": data.get("currency"),
        "cash": float(data.get("cash", 0)),
        "equity": float(data.get("equity", 0)),
        "buying_power": float(data.get("buying_power", 0)),
        "portfolio_value": float(data.get("portfolio_value", 0))
    }

    return jsonify(cleaned), 200