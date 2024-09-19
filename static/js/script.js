function fetchMarketData() {
    fetch('/api/market_data')
        .then(response => response.json())
        .then(data => {
            document.getElementById('last-price').textContent = data.spot_price;
            document.getElementById('price-change').textContent = data.mark_change_24h + '%';
        })
        .catch(error => console.error('Error fetching market data:', error));
}

// Fetch data every 1 second (1000 ms)
setInterval(fetchMarketData, 1000);

// Initial fetch
fetchMarketData();

