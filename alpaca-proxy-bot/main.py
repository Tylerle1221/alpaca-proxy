from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your real Alpaca keys
ALPACA_KEY_ID = 'PKSOB352J0MW1TOIECD6'
ALPACA_SECRET_KEY = 'hujr7cgZERs0NYSCzHYBvF5sHDEQxXFJK872UC4y'

# Example: proxy to get account info
@app.route('/alpaca/account', methods=['GET'])
def proxy_account():
    alpaca_url = 'https://paper-api.alpaca.markets/v2/account'

    headers = {
        'APCA-API-KEY-ID': ALPACA_KEY_ID,
        'APCA-API-SECRET-KEY': ALPACA_SECRET_KEY
    }

    alpaca_response = requests.get(alpaca_url, headers=headers)

    return jsonify(alpaca_response.json()), alpaca_response.status_code

# Example: proxy to submit an order
@app.route('/alpaca/order', methods=['POST'])
def proxy_order():
    alpaca_url = 'https://paper-api.alpaca.markets/v2/orders'

    headers = {
        'APCA-API-KEY-ID': ALPACA_KEY_ID,
        'APCA-API-SECRET-KEY': ALPACA_SECRET_KEY,
        'Content-Type': 'application/json'
    }

    # Forward the JSON body from the bot to Alpaca
    response = requests.post(alpaca_url, headers=headers, json=request.json)

    return jsonify(response.json()), response.status_code

@app.route('/')
def home():
    return '✅ Alpaca Proxy is running!'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
