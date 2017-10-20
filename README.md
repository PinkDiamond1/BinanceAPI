# Binance Python API integration

I've created an easy to use python integration with Binance's API. It enables developers to skip over the lower level API programming and jump right into the fun stuff like getting prices and trading cryptocurrencies. I'm also demonstrating how to begin automating this process and make a "connected" trading bot. You can do things like: Populate a Google Drive spreadsheet with your trade results, and send your phone a push notification showing your profit when your trade order is filled.

#### Installation
    git clone https://github.com/lampshade9909/BinanceAPI

#### Dependencies
	pip install websocket-client (https://pypi.python.org/pypi/websocket-client)

#### To run examples
	# Choose which function to call via uncommenting/commenting the source within examples.py, then run:
	python examples.py
	
	# Choose which websocket URL to subscribe to via uncommenting/commenting the source within examples_websockets.py, then run:
	python examples_websockets.py 
	
	
#### Import the library
	import binance
	
#### Set your API Key and Secret	
	binance.SetAPIKey("APIKeyGoesHere")
	binance.SetAPISecret("APISecretGoesHere")
	
####  Get orders for a symbol
	binance.API_Get_Orders_Binance("BNBETH")
	
####  Get the top 10 bids and/or asks for a symbol
	topNBids = binance.API_Get_TopNOrders_Binance("BNBETH", 10, "bids")
	topNAsks = binance.API_Get_TopNOrders_Binance("BNBETH", 10, "asks")
	topNBids, topNAsks = binance.API_Get_TopNOrders_Binance("BNBETH", 10, "both")

####  Get account info, free/locked balances, etc
	allInfo = binance.API_Get_AccountInfo_Binance()
	
	# Or get one at a time
	balance_bnb = binance.API_Get_Balance_Binance("bnb")
	balance_eth = binance.API_Get_Balance_Binance("eth")
	# balance_bnb = {u'locked': u'0.00000000', u'asset': u'BNB', u'free': u'2.99593206'}
	# balance_eth = {u'locked': u'0.00000000', u'asset': u'ETH', u'free': u'0.03479956'}
	
####  Get all prices
	allPrices = binance.API_Get_Markets_Binance()
	
	# Or get one price at a time
	BNB = binance.API_Get_Price_Binance("BNB")
	# BNB = {u'symbol': u'BNBBTC', u'price': u'0.00022507'}
	
####  Buy limit order
	binance.API_Post_BuyLimitOrder_Binance("SNTETH", 131, "0.00008111")
	
	#{
	#  u'orderId': 1866448,
	#  u'clientOrderId': u'e6NxhMuCxnqUtVJ2AfKkuV',
	#  u'origQty': u'131.00000000',
	#  u'symbol': u'SNTETH',
	#  u'side': u'BUY',
	#  u'timeInForce': u'GTC',
	#  u'status': u'NEW',
	#  u'transactTime': 1508458538408,
	#  u'type': u'LIMIT',
	#  u'price': u'0.00008111',
	#  u'executedQty': u'0.00000000'
	#}
	
####  Sell limit order
	binance.API_Post_SellLimitOrder_Binance("SNTETH", 120, "0.00009049")
	
####  Buy market order
	binance.API_Post_BuyMarketOrder_Binance("SNTETH", 30)
	
####  Sell market order
	binance.API_Post_SellMarketOrder_Binance("SNTETH", 50)

####  Buy limit iceberg order
	binance.API_Post_BuyLimitOrder_Binance("ETHBTC", 0.01, "0.054", 0.0025)
	
####  Sell market iceberg order
	binance.API_Post_SellMarketOrder_Binance("ETHBTC", 0.01, 0.0025)

####  Get the status of an order, given orderId
	binance.API_Get_OrderStatus_Binance("SNTETH", "1866448")
	
	#{
	#  u'orderId': 1866448,
	#  u'clientOrderId': u'e6NxhMuCxnqUtVJ2AfKkuV',
	#  u'origQty': u'131.00000000',
	#  u'icebergQty': u'0.00000000',
	#  u'symbol': u'SNTETH',
	#  u'side': u'BUY',
	#  u'timeInForce': u'GTC',
	#  u'status': u'NEW',
	#  u'stopPrice': u'0.00000000',
	#  u'time': 1508458538408,
	#  u'type': u'LIMIT',
	#  u'price': u'0.00008111',
	#  u'executedQty': u'0.00000000'
	#}

####  Delete an open order
	binance.API_Delete_Order_Binance("SNTETH", "1866448")
	
	#{
	#  u'orderId': 1866448,
	#  u'clientOrderId': u'IpNsmi8RPaYcXXDXjxoscN',
	#  u'symbol': u'SNTETH',
	#  u'origClientOrderId': u'e6NxhMuCxnqUtVJ2AfKkuV'
	#}
	
####  Get open orders
	binance.API_Get_OpenOrders_Binance("SNTETH")

####  Get order history
	binance.API_Get_TradeHistory_Binance("SNTETH")

####  Get 24 hour ticker price change stats
	binance.API_Get_24TickerPriceChange_Binance("SNTETH")

####  Get Kline/Candlestick data given interval
	binance.API_Get_KlineCandlestick_Binance("SNTETH", "30m")

####  Get aggregate trades
	binance.API_Get_AggregateTrades_Binance("SNTETH")
	
####  Automate your Binance trading experience with Stringify	
![alt text](https://i.imgur.com/RydTB09.png)

####  Here's how you do it
	# Use the API_Post_Stringify call to automate logging to help you track profits, transactions, balances, etc. You can even connect other physical/digital services like Google Drive, phone notifications, Twitter, Facebook, etc. 
	# Here, i've connected my Google Drive spreadsheet and my iPhone/Android device's notifications.  So everytime my program makes a trade, it sends me a notification and logs it to Google Drive.  
	# Binance's API + automation = fun.
	
	stringifyMakerURLgoesHere = "https://webhooks.stringify.com/v1/events/fEKBTcS1iCb3F99yGsNpV9svvetMzGwG/1/8a6e11d394fb9ac1af60b789d6e95537/TMSooXKVpJNRZ5choay3"
	API_Post_Stringify("Bought 100 BNB on Binance!", stringifyMakerURLgoesHere)
	

I, Joey Zacherl, fully own the code I submit.  I guarantee there are no copyright or license restrictions.  I further agree any code I submit will be in public domain.  Anyone can copy, change, derive further work from it without any restrictions.