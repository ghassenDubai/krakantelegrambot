import ccxt

# Initialize the Kraken API
kraken = ccxt.kraken()

try:
    # Get ticker information for the BTC/USD pair
    ticker = kraken.fetch_ticker('BTC/USD')

    # Print the ticker information
    print("Ticker for BTC/USD:")
    print("Last Price:", ticker['last'])
    print("High:", ticker['high'])
    print("Low:", ticker['low'])
    print("Volume:", ticker['baseVolume'])

except ccxt.NetworkError as e:
    print(f"Network error: {e}")
except ccxt.ExchangeError as e:
    print(f"Exchange error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
