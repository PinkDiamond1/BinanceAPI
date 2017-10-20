# Binance Python API integration

I've created an easy to use python integration with [Binance's API](https://www.binance.com/). It enables developers to skip over the lower level API programming and jump right into the fun stuff like getting prices and trading cryptocurrencies. I'm also demonstrating how to begin automating this process and make a "connected" trading bot. You can do things like: Populate a Google Drive spreadsheet with your trade results, and send your phone a push notification showing your profit when your trade order is filled. 

This library is very easy to use, has a built in logging mechanism, does the heavy lifting with all of your Binance's APIs, and introduces developers to powerful automation features that can be tied into your program.

I, Joey Zacherl, fully own the code I submit.  I guarantee there are no copyright or license restrictions.  I further agree any code I submit will be in public domain.  Anyone can copy, change, derive further work from it without any restrictions.

#### Installation
    git clone https://github.com/lampshade9909/BinanceAPI

#### Dependencies
	pip install websocket-client (https://pypi.python.org/pypi/websocket-client)
	pip install requests
	brew install coreutils (I'm using gdate to get time in milliseconds)

#### Import the library
	import binance
	
#### To run examples
	# Choose which function to call via uncommenting/commenting the source within examples.py, then run:
	python examples.py
	
	# Choose which websocket URL to subscribe to via uncommenting/commenting the source within examples_websockets.py, then run:
	python examples_websockets.py 
	
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
	
####  Get prices
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

####  Get the status of an order
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
	
####  Websockets
    websocket.enableTrace(True)

    # Choose which URL you'd like to subscribe to
    url = "wss://stream.binance.com:9443/ws/ethbtc@depth"
    ws = websocket.WebSocketApp(url, on_message = on_message, on_error = on_error, on_close = on_close)
    ws.on_open = on_open
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
	
	--- response header --- 
	HTTP/1.1 101 Switching Protocols 
	Date: Fri, 20 Oct 2017 00:54:25 GMT 
	Connection: upgrade 
	Expires: Thu, 01 Jan 1970 00:00:01 GMT 
	Cache-Control: no-cache, no-store, must-revalidate 
	Upgrade: WebSocket 
	Sec-WebSocket-Accept: eUVrgdbvaqvV5ku28oQKabQ3S2U= 
	----------------------- 
	{"e":"depthUpdate","E":1508460865901,"s":"ETHBTC","U":17570121,"u":17570130,"b":[["0.05383600","0.00000000",[]],["0.05382000","10.10900000",[]],["0.05099200","2.25000000",[]]],"a":[["0.05406100","15.00000000",[]],["0.05406200","0.00000000",[]],["0.05406600","0.00000000",[]],["0.05406700","0.00000000",[]],["0.05686700","0.00000000",[]]]}
	
	{"e":"depthUpdate","E":1508460866901,"s":"ETHBTC","U":17570131,"u":17570138,"b":[["0.05382400","10.20900000",[]],["0.05382000","0.00000000",[]],["0.05099200","0.00000000",[]]],"a":[["0.05406000","15.00000000",[]],["0.05406100","0.00000000",[]],["0.05683400","18.30100000",[]]]}
	
	{"e":"depthUpdate","E":1508460867901,"s":"ETHBTC","U":17570139,"u":17570142,"b":[],"a":[["0.05405900","14.95000000",[]],["0.05406000","0.00000000",[]]]}
	
	{"e":"depthUpdate","E":1508460868902,"s":"ETHBTC","U":17570143,"u":17570147,"b":[["0.05382500","10.35900000",[]],["0.05382400","0.00000000",[]],["0.05101500","11.25000000",[]]],"a":[["0.05405800","15.00000000",[]],["0.05405900","0.00000000",[]]]}
	
	{"e":"depthUpdate","E":1508460869902,"s":"ETHBTC","U":17570148,"u":17570152,"b":[["0.05384400","10.35900000",[]],["0.05382500","0.00000000",[]]],"a":[["0.05405800","0.00000000",[]],["0.05406200","15.00000000",[]],["0.05428300","0.00000000",[]]]}

From here, you can update your UI or your program's behavior with this real-time data from websockets.

Note: this library generates a log file called "logfile" which helps you debug and track transactions.

####  Automate your Binance trading experience with Stringify	
![alt text](https://i.imgur.com/RydTB09.png)

"When my bot makes a trade, send my phone a notification and log it to a Google Drive spreadsheet."

Binance's API + Automation = fun. Use the API_Post_Stringify call to automate logging to help you track profits, transactions, balances, etc. You can even connect other physical/digital services like Google Drive, phone notifications, Twitter, Facebook, etc. 
Here, i've connected my Google Drive spreadsheet and my iPhone/Android notifications. So everytime my bot makes a trade, it sends me a notification and logs it to Google Drive. I can use this to track profits and make sure it's running properly. 

	stringifyMakerURLgoesHere = "https://webhooks.stringify.com/v1/events/fEKBTcS1iCb3F99yGsNpV9svvetMzGwG/1/8a6e11d394fb9ac1af60b789d6e95537/TMSooXKVpJNRZ5choay3"
	API_Post_Stringify("Bought 100 BNB on Binance!", stringifyMakerURLgoesHere)
	
![alt text](https://i.imgur.com/yxtboiV.png)

Set up a [Stringify account](https://www.stringify.com/) with your iOS or Android mobile device. You can download it in the App Store or Google Play. 

Next, import this flow: ["When my bot makes a trade, send my phone a notification and log it to a Google Drive spreadsheet."](https://app.stringify.com/flow/ebtuMIcbGogPxvr7Etlh)

![alt text](https://i.imgur.com/m8TSfvO.png)

Your Binance trading bot will be the trigger on the left. It will trigger this automation and pass a message to your phone notification or Google Drive thing on the right. 

![alt text](https://i.imgur.com/vWiofnw.png)

The Maker thing on the left generates a URL to which the API_Post_Stringify method can make a REST request.

![alt text](https://i.imgur.com/MssRmyy.png)![alt text](https://i.imgur.com/J5lRaCc.png)
The notification and Google Drive things get configured such that the data from the Binance bot gets sent to them. 