from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Use environment variables for Alpaca credentials
ALPACA_KEY_ID = os.environ.get('ALPACA_KEY_ID')
ALPACA_SECRET_KEY = os.environ.get('ALPACA_SECRET_KEY')

@app.route('/alpaca/account', methods=['GET'])
def proxy_account():
    _ = request.headers.get("X-API-KEY")  # Accept and ignore X-API-KEY  # Not used, but accepted
    alpaca_url = 'https://paper-api.alpaca.markets/v2/account'
    headers = {
        'APCA-API-KEY-ID': ALPACA_KEY_ID,
        'APCA-API-SECRET-KEY': ALPACA_SECRET_KEY
    }
    response = requests.get(alpaca_url, headers=headers)
    return jsonify(response.json()), response.status_code

@app.route('/alpaca/order', methods=['POST'])
def proxy_order():
    _ = request.headers.get("X-API-KEY")  # Accept and ignore X-API-KEY  # Not used, but accepted
    alpaca_url = 'https://paper-api.alpaca.markets/v2/orders'
    headers = {
        'APCA-API-KEY-ID': ALPACA_KEY_ID,
        'APCA-API-SECRET-KEY': ALPACA_SECRET_KEY,
        'Content-Type': 'application/json'
    }
    response = requests.post(alpaca_url, headers=headers, json=request.json)
    return jsonify(response.json()), response.status_code


@app.route('/')
def home():
    return '✅ Alpaca Proxy is running!'

# IMPORTANT: Render requires binding to 0.0.0.0 and using the PORT env variable
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Fallback just in case
    app.run(host='0.0.0.0', port=port)
