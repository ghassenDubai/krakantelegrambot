from datetime import time

from krakenex import API

# Initialize the Kraken API client
kraken = API('ecYBiCizQp3g9wSk38CaPhplrtPFp6LP7UqmuUMzBj+CvzpAod52iboc'
             , '2TNJT3aYP0mtAETY/KU5GVFH0C7NKoxxQ+hyl0jOQ3JPwiAk4aYuMNKqxHc+9ykCXQlxiiJJyLOVuANZASycNA==')

def get_balance():
    try:
        # Get standard balance information
        extended_balance = kraken.query_private('Balance', {'asset': 'all'})

        return extended_balance


    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Usage example:
# Replace 'your_api_key' and 'your_api_secret' with your actual Kraken API key and secret
#print(get_balance())
def get_extended_balance():
    try:
        # Get extended balance information
        extended_balance_response = kraken.query_private('Balance', {'asset': 'all'})

        # Print or process the extended balance response as needed
       # print("Extended Balance:")
       # print(extended_balance_response)


        return extended_balance_response

    except Exception as e:
        return f"An unexpected error occurred: {e}"

print(get_extended_balance())




def get_trade_balance():
    try:
        # Fetch trade balance information
        trade_balance_response = kraken.query_private('TradeBalance')

        # Print or process the trade balance as needed
        print("Trade Balance:")
        print(trade_balance_response)

        return trade_balance_response

    except Exception as e:
        return f"An unexpected error occurred: {e}"
#get_trade_balance()
def get_open_orders():
    try:
        # Fetch open orders
        open_orders_response = kraken.query_private('OpenOrders')

        # Print or process the open orders as needed
        print("Open Orders:")
        print(open_orders_response)

        return open_orders_response

    except Exception as e:
        return f"An unexpected error occurred: {e}"
#get_open_orders()
def get_closed_orders():
    try:
        # Fetch closed orders
        closed_orders_response = kraken.query_private('ClosedOrders')

        # Print or process the closed orders as needed
        print("Closed Orders:")
        print(closed_orders_response)

        return closed_orders_response

    except Exception as e:
        return f"An unexpected error occurred: {e}"
#get_closed_orders()

def get_orders_info(order_ids):
    try:
        # Fetch information about specific orders
        orders_info_response = kraken.query_private('QueryOrders', {'txid': order_ids})

        # Print or process the orders information as needed
        print("Orders Information:")
        print(orders_info_response)

        return orders_info_response

    except Exception as e:
        return f"An unexpected error occurred: {e}"

#order_ids_to_query = ['TWYHO4-YJB2N-KJP3OW']
#get_orders_info(order_ids_to_query)

def get_trade_history(pair='XBTUSD', since=None):
    try:
        # Parameters for the TradesHistory endpoint
        params = {'pair': pair}
        if since is not None:
            params['since'] = since

        # Get trade history
        trade_history_response = kraken.query_private('TradesHistory', params)

        # Check if there are no errors
        if not trade_history_response['error']:
            # Print or process the trade history result
            print("Trade History:")
            print(trade_history_response['result']['trades'])

            return trade_history_response['result']['trades']
        else:
            print("Error:", trade_history_response['error'])
            return None

    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Usage example:
# Replace 'your_api_key' and 'your_api_secret' with your actual Kraken API key and secret
#get_trade_history(pair='XBTUSD')

def get_trade_info(trade_id):
    try:
        # Fetch information about a specific trade
        trade_info_response = kraken.query_private('QueryTrades', {'txid': trade_id})

        # Print or process the trade information as needed
        print(f"Trade Information for Trade ID {trade_id}:")
        print(trade_info_response)

        return trade_info_response

    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Usage example:OKKK
# Replace 'your_api_key' and 'your_api_secret' with your actual Kraken API key and secret
# Replace 'your_trade_id' with the actual trade ID you want to query

#get_trade_info("TWYHO4-YJB2N-KJP3OW")
def get_open_positions():
    try:
        # Fetch open positions (note: Kraken API may not have a direct endpoint for open positions)
        open_positions_response = kraken.query_private('OpenPositions')

        # Print or process the open positions as needed
        print("Open Positions:")
        print(open_positions_response)

        return open_positions_response

    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Usage example:
# Replace 'your_api_key' and 'your_api_secret' with your actual Kraken API key and secret
#get_open_positions()

def get_assets_info():
    try:
        # Fetch information about assets
        assets_info_response = kraken.query_public('Assets')

        # Print or process the assets information as needed
        print("Assets Information:")
        print(assets_info_response)

        return assets_info_response

    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Usage example:
# No need for API key and secret for public endpoints
#get_assets_info()


def get_tradable_asset_pairs():
    try:
        # Fetch information about tradable asset pairs
        tradable_asset_pairs_response = kraken.query_public('AssetPairs')

        # Print or process the tradable asset pairs information as needed
        print("Tradable Asset Pairs:")
        print(tradable_asset_pairs_response)

        return tradable_asset_pairs_response

    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Usage example:
# No need for API key and secret for public endpoints
#get_tradable_asset_pairs()

def get_minimum_volume(asset_pair):
    try:
        # Simulated: Fetch information about the specified asset pair and extract minimum volume
        asset_pair_info_response = kraken.query_public('AssetPairs', {'pair': asset_pair})
        minimum_volume = asset_pair_info_response['result'][asset_pair]['ordermin']

        # Print or process the minimum volume as needed
        print(f"Minimum Volume for {asset_pair}: {minimum_volume}")

        return minimum_volume

    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Usage example: OKK
# No need for API key and secret for public endpoints
# Replace 'your_asset_pair' with the actual asset pair you want to query (e.g., 'XBT/USD')
#get_minimum_volume('XETHXXBT')

def get_market_price(asset_pair):
    try:
        print('dddd')
        # Fetch ticker information for the specified asset pair
        ticker_response = kraken.query_public('Ticker', {'pair': asset_pair})
        market_price = ticker_response['result'][asset_pair]['c'][0]

        # Print or process the market price as needed
        print(f"Market Price for {asset_pair}: {market_price}")

        return market_price

    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Usage example: OKKK
# No need for API key and secret for public endpoints
# Replace 'your_asset_pair' with the actual asset pair you want to query (e.g., 'XBT/USD')
#get_market_price('XXBTZUSD')





def cancel_order(order_id):
    try:
        # Cancel the specified order
        cancel_order_response = kraken.query_private('CancelOrder', {'txid': order_id})

        # Print or process the cancel order response as needed
        print(f"Cancel Order Response for Order ID {order_id}:")
        print(cancel_order_response)

        return cancel_order_response

    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Usage example:
# Replace 'your_api_key' and 'your_api_secret' with your actual Kraken API key and secret
# Replace 'your_order_id' with the actual order ID you want to cancel
#order_id_to_cancel = 'your_order_id'
#cancel_order(order_id_to_cancel)

def cancel_all_orders():
    try:
        # Fetch all open orders
        open_orders_response = kraken.query_private('OpenOrders')

        # Extract order IDs from the open orders response
        order_ids = [order_id for order_id in open_orders_response['result']['open'].keys()]

        # Cancel each open order
        for order_id in order_ids:
            cancel_order_response = kraken.query_private('CancelOrder', {'txid': order_id})
            print(f"Cancel Order Response for Order ID {order_id}:")
            print(cancel_order_response)

        return "All open orders canceled successfully."

    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Usage example:
# Replace 'your_api_key' and 'your_api_secret' with your actual Kraken API key and secret
#cancel_all_orders()

def cancel_all_orders_after_x_seconds(delay_seconds):
    try:
        # Fetch all open orders
        open_orders_response = kraken.query_private('OpenOrders')

        # Extract order IDs from the open orders response
        order_ids = [order_id for order_id in open_orders_response['result']['open'].keys()]

        # Introduce a delay
        time.sleep(delay_seconds)

        # Cancel each open order
        for order_id in order_ids:
            cancel_order_response = kraken.query_private('CancelOrder', {'txid': order_id})
            print(f"Cancel Order Response for Order ID {order_id}:")
            print(cancel_order_response)

        return "All open orders canceled after the specified delay."

    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Usage example:
# Replace 'your_api_key' and 'your_api_secret' with your actual Kraken API key and secret
# Replace 60 with the desired delay in seconds
#cancel_all_orders_after_x_seconds(60)

def get_deposit_methods(asset):
    try:
        # Fetch deposit methods for the specified asset
        deposit_methods_response = kraken.query_private('DepositMethods', {'asset': asset})

        # Check if the response contains valid data
        if 'result' in deposit_methods_response and 'methods' in deposit_methods_response['result']:
            # Print or process the deposit methods response as needed
            print(f"Deposit Methods for {asset}:")
            print(deposit_methods_response['result']['methods'])
            return deposit_methods_response

        # Print an error message if the response does not contain valid data
        print(f"Error: Unable to retrieve deposit methods for {asset}. Response: {deposit_methods_response}")
        return deposit_methods_response

    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Usage example:
# Replace 'your_api_key' and 'your_api_secret' with your actual Kraken API key and secret
# Replace 'XBT' with the desired asset code
#get_deposit_methods('XBT')

def get_deposit_addresses(asset='XBT', method='Bitcoin', new=True):
    try:
        # Fetch deposit addresses for the specified asset and method
        deposit_addresses_response = kraken.query_private('DepositAddresses', {'asset': asset, 'method': method, 'new': new})

        # Print or process the deposit addresses response as needed
        print(f"Deposit Addresses for {asset} using {method}:")
        print(deposit_addresses_response)

        return deposit_addresses_response

    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Usage example:
# Replace 'your_api_key' and 'your_api_secret' with your actual Kraken API key and secret
# Replace 'XBT', 'Bitcoin', and True with the desired parameters
#get_deposit_addresses(asset='XBT', method='Bitcoin', new=True)

def make_withdrawal_request(asset='XBT', key='', address='', amount='0.05'):
    try:
        # Make a withdrawal request
        withdrawal_request_response = kraken.query_private('Withdraw', {
            'asset': asset,
            'key': key,      # Replace with the withdrawal key (if applicable)
            'address': address,
            'amount': amount,
        })

        # Print or process the withdrawal request response as needed
        print(f"Withdrawal Request Response for {amount} {asset} to {address}:")
        print(withdrawal_request_response)

        return withdrawal_request_response

    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Usage example:
# Replace 'your_api_key' and 'your_api_secret' with your actual Kraken API key and secret
# Replace 'XBT', '', 'withdrawal_address', and '0.05' with the desired parameters
#make_withdrawal_request(asset='XBT', key='', address='withdrawal_address', amount='0.05')

def get_recent_deposits_status():
    try:
        # Get the status of recent deposits
        deposit_status_response = kraken.query_private('DepositStatus')

        # Print or process the deposit status response as needed
        print("Recent Deposit Status:")
        print(deposit_status_response)

        return deposit_status_response

    except Exception as e:
        return f"An unexpected error occurred: {e}"


# Usage example:
# Replace 'your_api_key' and 'your_api_secret' with your actual Kraken API key and secret
#get_recent_deposits_status()


def get_recent_withdrawal_status():
    try:
        # Get the status of recent withdrawals
        withdrawal_status_response = kraken.query_private('WithdrawStatus')

        # Check if the response contains valid data
        if 'result' in withdrawal_status_response and withdrawal_status_response['result']:
            # Print or process the withdrawal status response as needed
            print("Recent Withdrawal Status:")
            print(withdrawal_status_response)

            return withdrawal_status_response

        # Print an error message if the response does not contain valid data
        print(f"Error: Unable to retrieve recent withdrawal status. Response: {withdrawal_status_response}")
        return withdrawal_status_response

    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Usage example:
# Replace 'your_api_key' and 'your_api_secret' with your actual Kraken API key and secret
#get_recent_withdrawal_status()

# Usage example:

# Usage example:
# Replace 'your_api_key' and 'your_api_secret' with your actual Kraken API key and secret
#get_balance()
#get_extended_balance()
#get_trade_balance()
#get_open_orders()
#get_closed_orders()


