import json
import requests
import telebot
import Api_Integration

TOKEN = '6732986203:AAHGwlfWWgxTR06libiEOZyMDB1nrCiYwjU'
bot = telebot.TeleBot(TOKEN, parse_mode=None)
quantity = 0
def send_file(chat_id,file_path):
    url = f'https://api.telegram.org/bot{TOKEN}/sendDocument'
    data = {'chat_id': chat_id}
    files = {'document': open(file_path, 'rb')}
    requests.post(url, data=data, files=files)

# httpstatuscode 400: error client/ server error 500 / 200 successful/ 100:information/300/:transformation
@bot.message_handler(commands=['start', 'new', 'exit'])
def send_welcome(message):
    if message.text == '/exit':
        bot.send_message(message.chat.id, "Goodbye! Click Start to restart the bot")
        # Optionally, you can stop the bot using sys.exit() or some other method.
        # Here, I'm just returning without stopping, as stopping might depend on your bot setup.
        return
    msg = bot.reply_to(message, "/getBalance "
                                "\n/getExtendedBalance\n/getTradeBalance\n/getOpenOrders\n/getClosedOrders"
                                "\n/getOrdersInfo"
                                "\n/getTradeHistory\n/getTradeInfo\n/getOpenPositions"
                                "\n/getAssetsInfo\n/getTradableAssetPairs\n/getMinimumVolume\n/getMarketPrice"
                                "\n/editOrder\n/cancel_order \n/cancel_all_orders"
                                "\n/cancelAllOrdersAfterX"
                                "\n/getDepositMethods"
                                "\n/getDepositAddresses\n/makeWithdrawalRequest\n/getRecentDepositsStatus"
                                "\n/getRecentWithrawalStatus"
                                "\n/exit ")
    bot.register_next_step_handler(msg, start)

# Select command
def start(message):
    chat_id = message.chat.id
    option = message.text
    if option == "/getBalance":
        result = Api_Integration.get_balance()
        resultB = result['result']
        with open("Balance.json", "w") as f:
            f.write(json.dumps(resultB, indent=4))
            f.close()
        send_file(chat_id, 'Balance.json')

    elif option == "/getExtendedBalance":
        result = Api_Integration.get_extended_balance()
        resultB = result['result']
        with open("ExtendedBalance.json", "w") as f:
            f.write(json.dumps(resultB, indent=4))
            f.close()
        send_file(chat_id, 'ExtendedBalance.json')

    elif option == "/getTradeBalance":
        result = Api_Integration.get_trade_balance()
        resultB = result['result']
        with open("TradeBalance.json", "w") as f:
            f.write(json.dumps(resultB, indent=4))
            f.close()
        send_file(chat_id, 'TradeBalance.json')

    elif option == "/getOpenOrders":
        result = Api_Integration.get_open_orders()
        resultB = result['result']
        with open("getOpenOrders.json", "w") as f:
            f.write(json.dumps(resultB, indent=4))
            f.close()
        send_file(chat_id, 'getOpenOrders.json')

    elif option == "/getClosedOrders":
        result = Api_Integration.get_closed_orders()

        with open("getClosedOrders.json", "w") as f:
            f.write(json.dumps(result, indent=4))
            f.close()
        send_file(chat_id, 'getClosedOrders.json')

    elif option == "/getOrdersInfo":
        msg= bot.send_message(chat_id,"Enter orderID please")
        bot.register_next_step_handler(msg,getOrdersInfo)

    elif option == "/getTradeHistory":
        msg= bot.send_message(chat_id,"Enter Pair please")
        bot.register_next_step_handler(msg,getTradeHistory)

    elif option == "/getTradeInfo":
        msg= bot.send_message(chat_id,"Enter TradeID please")
        bot.register_next_step_handler(msg,getTradeInfo)

    elif option == "/getOpenPositions":
        result = Api_Integration.get_open_positions()
        with open("OpenPositions.json", "w") as f:
            f.write(json.dumps(result, indent=4))
            f.close()
        send_file(chat_id, 'OpenPositions.json')

    elif option == "/getAssetsInfo":
        result = Api_Integration.get_assets_info()
        with open("AssetsInfo.json", "w") as f:
            f.write(json.dumps(result, indent=4))
            f.close()
        send_file(chat_id, 'AssetsInfo.json')
    elif option == "/getTradableAssetPairs":
        result = Api_Integration.get_tradable_asset_pairs()
        with open("TradableAssetPairs.json", "w") as f:
            f.write(json.dumps(result, indent=4))
            f.close()
        send_file(chat_id, 'TradableAssetPairs.json')

    elif option == "/getMinimumVolume":
        msg= bot.send_message(chat_id,"Enter your_asset_pair please")
        bot.register_next_step_handler(msg,getMinimumVolume)

    elif option == "/getMarketPrice":
        msg = bot.send_message(chat_id, "Enter your_asset_pair please")
        bot.register_next_step_handler(msg, getMarketPrice)

    elif option == "/cancel_order":
        msg = bot.send_message(chat_id, "Enter orderID please")
        bot.register_next_step_handler(msg, cancel_order)

    elif option == "/cancel_all_orders":
        result = Api_Integration.cancel_all_orders()
        bot.send_message(chat_id,result)

    elif option == "/cancelAllOrdersAfterX":
        msg = bot.send_message(chat_id, "Enter specified delay please")
        bot.register_next_step_handler(msg, cancelAllOrdersAfterX)

    elif option == "/getDepositMethods":
        msg = bot.send_message(chat_id, "Enter assets please")
        bot.register_next_step_handler(msg, getDepositMethods)

    elif option == "/getDepositAddresses":
        msg = bot.send_message(chat_id, "Enter assets please")
        bot.register_next_step_handler(msg, getasset)

    elif option == "/makeWithdrawalRequest":
        msg = bot.send_message(chat_id, "Enter assets please")
        bot.register_next_step_handler(msg, getassetR)

    elif option == "/getRecentDepositsStatus":
        result = Api_Integration.get_recent_deposits_status()
        with open("getRecentDepositsStatus.json","w") as f:
            f.write(json.dumps(result, indent = 4))
            f.close()
        send_file(chat_id,'getRecentDepositsStatus.json')

    elif option == "/getRecentWithrawalStatus":
        result = Api_Integration.get_recent_deposits_status()
        with open("RecentWithrawalStatus.json","w") as f:
            f.write(json.dumps(result, indent = 4))
            f.close()
        send_file(chat_id,'RecentWithrawalStatus.json')

    else:
        msg = bot.send_message(chat_id, "Error choose a valid option")
        bot.register_next_step_handler(msg, start)





def getOrdersInfo(message):
    chat_id=message.chat.id
    orderId=message.text
    result=Api_Integration.get_orders_info(orderId)
    with open("OrdersInfo.json", "w") as f:
        f.write(json.dumps(result, indent=4))
        f.close()
    send_file(chat_id, 'OrdersInfo.json')

def getTradeHistory(message):
    chat_id = message.chat.id
    pair = message.text
    result = Api_Integration.get_trade_history(pair=pair)
    with open("TradeHistory.json", "w") as f:
        f.write(json.dumps(result, indent=4))
        f.close()
    send_file(chat_id, 'TradeHistory.json')


def getTradeInfo(message):
    chat_id=message.chat.id
    tradeId=message.text
    result=Api_Integration.get_orders_info(tradeId)
    with open("TradeInfo.json", "w") as f:
        f.write(json.dumps(result, indent=4))
        f.close()
    send_file(chat_id, 'TradeInfo.json')

def getMinimumVolume(message):
    chat_id = message.chat.id
    pair = message.text
    result = Api_Integration.get_minimum_volume(pair)
    bot.send_message(chat_id,result)

def getMarketPrice(message):
    chat_id = message.chat.id
    pair = message.text
    result = Api_Integration.get_market_price(pair)
    bot.send_message(chat_id, result)

def cancel_order(message):
    chat_id = message.chat.id
    orderId = message.text
    result = Api_Integration.cancel_order(orderId)
    bot.send_message(chat_id, result)

def cancelAllOrdersAfterX(message):
    chat_id = message.chat.id
    delay = message.text
    result = Api_Integration.cancel_all_orders_after_x_seconds(delay)
    bot.send_message(chat_id, result)

def getDepositMethods(message):
    chat_id = message.chat.id
    asset = message.text
    result = Api_Integration.get_deposit_methods(asset)
    bot.send_message(chat_id, result)

def getasset(message):
    chat_id = message.chat.id
    global asset2
    asset2= message.text
    msg = bot.send_message(chat_id, "Enter method please:")
    bot.register_next_step_handler(msg, getmethod)

def getmethod(message):
    chat_id = message.chat.id
    method = message.text
    result = Api_Integration.get_deposit_addresses(asset=asset2,method=method,new=True)
    with open("deposit_addresses.json", "w") as f:
        f.write(json.dumps(result, indent=4))
        f.close()
    send_file(chat_id, 'deposit_addresses.json')

def getassetR(message):
    chat_id = message.chat.id
    global asset3
    asset3 = message.text
    msg = bot.send_message(chat_id, "Enter address please:")
    bot.register_next_step_handler(msg, getaddress)

def getaddress(message):
    chat_id = message.chat.id
    global address
    address = message.text
    msg = bot.send_message(chat_id, "Enter amount please:")
    bot.register_next_step_handler(msg, getamount)

def getamount(message):
    chat_id = message.chat.id
    global amount
    amount = message.text
    result= Api_Integration.make_withdrawal_request(asset=asset3, key='', address=address, amount=amount)
    with open("makeWithdrawalRequest.json","w")as f:
        f.write(json.dumps(result,indent=4))
        f.close()
    send_file(chat_id,"makeWithdrawalRequest.json")



















# Polling without webhook
bot.polling(non_stop=True, timeout=0, none_stop=True, skip_pending=True)
'''
bot.enable_save_next_step_handlers(delay=0)
bot.load_next_step_handlers()
bot.polling(non_stop=True, timeout=0, none_stop=True, skip_pending=True)
'''