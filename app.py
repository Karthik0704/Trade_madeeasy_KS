from flask import Flask, render_template, jsonify
from utils.api_handler import get_market_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/market_data')
def market_data():
    # Fetch BTC/USD market data
    data = get_market_data()
    if data:
        return jsonify(data)
    else:
        return jsonify({'error': 'Error fetching market data'}), 500

if __name__ == '__main__':
    app.run(debug=True)
