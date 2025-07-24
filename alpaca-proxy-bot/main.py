from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace these with your real Alpaca paper keys
ALPACA_KEY_ID = 'PKSOB352J0MW1TOIECD6'
ALPACA_SECRET_KEY = 'hujr7cgZERs0NYSCzHYBvF5sHDEQxXFJK872UC4y'

@app.route('/alpaca/account', methods=['GET'])
def proxy_account():
    _ = request.headers.get("X-API-KEY")  # Dummy key to satisfy ChatGPT

    alpaca_url = 'https://paper-api.alpaca.markets/v2/account'
    headers = {
        'APCA-API-KEY-ID': ALPACA_KEY_ID,
        'APCA-API-SECRET-KEY': ALPACA_SECRET_KEY
    }

    response = requests.get(alpaca_url, headers=headers)

    print("DEBUG: Alpaca response:", response.json())  # Optional: log it in Render
    return jsonify(response.json()), response.status_code

@app.route('/')
def home():
    return '✅ Alpaca Proxy is running!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
