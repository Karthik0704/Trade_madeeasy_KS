import requests
from config import DELTA_API_KEY, DELTA_BASE_URL

def get_market_data(symbol='BTCUSD'):
    endpoint = f'{DELTA_BASE_URL}/v2/tickers'
    headers = {
        'Authorization': f'Bearer {DELTA_API_KEY}',
    }
    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        data = response.json()['result']
        for ticker in data:
            if ticker['symbol'] == symbol:
                return ticker
    except requests.RequestException as e:
        print(f'Error: {e}')
        return None