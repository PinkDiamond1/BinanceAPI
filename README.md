# Python Binance API integration

I've created an easy to use python integration with [Binance's API](https://www.binance.com/). It enables developers to skip over the lower level API programming and jump right into the fun stuff like getting prices and trading cryptocurrencies. I'm also demonstrating how to begin automating this process and make a "connected" trading bot. You can do things like: Populate a Google Drive spreadsheet with your trade results, and send your phone a push notification showing your profit when your trade order is filled. 

This library is very easy to use, has a built in logging mechanism, does the heavy lifting with all of your Binance's APIs, and introduces developers to powerful automation features that can be tied into your program. 

I, Joey Zacherl, fully own the code I submit.  I guarantee there are no copyright or license restrictions.  I further agree any code I submit will be in public domain.  Anyone can copy, change, derive further work from it without any restrictions.

#### Installation
    git clone https://github.com/lampshade9909/BinanceAPI

#### Dependencies
	pip install requests
	pip install websocket-client (Only needed if you're doing websockets, https://pypi.python.org/pypi/websocket-client)

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
	
#### Ping and server time
	# Ping the API
	binance.API_Get_Ping()
	# Get current Time
	binance.API_Get_Time()
<details><summary>Show Output</summary>
<pre>
{}
{u'serverTime': 1508517204492}
</pre>
</details>
	
#### Get orders for a symbol
	orders = binance.API_Get_Orders("BNBETH")
<details><summary>Show Output</summary>
<pre>
{
  u'lastUpdateId': 6602561,
  u'bids': [
    [
      u'0.00406001',
      u'36.00000000',
      []
    ],
    [
      u'0.00406000',
      u'89.00000000',
      []
    ]
	....
    [
      u'0.00311100',
      u'165.00000000',
      []
    ]
  ],
  u'asks': [
    [
      u'0.00410516',
      u'298.00000000',
      []
    ],
    [
      u'0.00410517',
      u'200.00000000',
      []
    ]
	...
    [
      u'0.00484999',
      u'1000.00000000',
      []
    ]
  ]
}
</pre>
</details>
	
####  Get the top n bids and/or asks for a symbol
	# Get to 10 in separate calls
	topNBids = binance.API_Get_TopNOrders("BNBETH", 10, "bids")
	topNAsks = binance.API_Get_TopNOrders("BNBETH", 10, "asks")
	# Get top 10 in one single call
	topNBids, topNAsks = binance.API_Get_TopNOrders("BNBETH", 10, "both")
<details><summary>Show Output</summary>
<pre>
topNBids = 
[
  [
    u'0.00410000',
    u'10.00000000',
    []
  ],
  [
    u'0.00406006',
    u'100.00000000',
    []
  ],
  [
    u'0.00405110',
    u'300.00000000',
    []
  ],
  [
    u'0.00405108',
    u'312.00000000',
    []
  ],
  [
    u'0.00405106',
    u'449.00000000',
    []
  ],
  [
    u'0.00405100',
    u'330.00000000',
    []
  ],
  [
    u'0.00405001',
    u'729.00000000',
    []
  ],
  [
    u'0.00405000',
    u'4241.00000000',
    []
  ],
  [
    u'0.00404019',
    u'1388.00000000',
    []
  ],
  [
    u'0.00404017',
    u'840.00000000',
    []
  ]
]
topNAsks = 
[
  [
    u'0.00410829',
    u'2000.00000000',
    []
  ],
  [
    u'0.00410830',
    u'324.00000000',
    []
  ],
  [
    u'0.00410837',
    u'200.00000000',
    []
  ],
  [
    u'0.00410880',
    u'1040.00000000',
    []
  ],
  [
    u'0.00414750',
    u'375.00000000',
    []
  ],
  [
    u'0.00414874',
    u'1000.00000000',
    []
  ],
  [
    u'0.00414999',
    u'4480.00000000',
    []
  ],
  [
    u'0.00415000',
    u'20.00000000',
    []
  ],
  [
    u'0.00418500',
    u'5.00000000',
    []
  ],
  [
    u'0.00418999',
    u'825.00000000',
    []
  ]
]
</pre>
</details>

####  Get account info, free/locked balances, etc
	# Get all account info
	allInfo = binance.API_Get_AccountInfo()
	# Or get only asset balances for one symbol at a time
	balance_bnb = binance.API_Get_Balance("bnb")
	balance_eth = binance.API_Get_Balance("eth")
<details><summary>Show Output</summary>
<pre>
allInfo = 
{
  u'buyerCommission': 0,
  u'canWithdraw': True,
  u'takerCommission': 10,
  u'canTrade': True,
  u'makerCommission': 10,
  u'balances': [
    {
      u'locked': u'0.00000000',
      u'asset': u'BTC',
      u'free': u'0.00053875'
    },
    {
      u'locked': u'0.00000000',
      u'asset': u'LTC',
      u'free': u'0.00000000'
    },
    {
      u'locked': u'0.00000000',
      u'asset': u'ETH',
      u'free': u'0.03479956'
    },
	...
    {
      u'locked': u'0.00000000',
      u'asset': u'DASH',
      u'free': u'0.00000000'
    }
  ],
  u'sellerCommission': 0,
  u'canDeposit': True
}

balance_bnb = {u'locked': u'0.00000000', u'asset': u'BNB', u'free': u'2.99593206'}
balance_eth = {u'locked': u'0.00000000', u'asset': u'ETH', u'free': u'0.03479956'}
</pre>
</details>
	
####  Get prices
	# One at a time
	BNB = binance.API_Get_Price("BNB")
	# All at once
	markets = binance.API_Get_Markets()
<details><summary>Show Output</summary>
<pre>
BNB = {u'symbol': u'BNBBTC', u'price': u'0.00021087'}

markets =
[
  {
    u'symbol': u'ETHBTC',
    u'price': u'0.05126100'
  },
  {
    u'symbol': u'LTCBTC',
    u'price': u'0.01018100'
  },
  {
    u'symbol': u'BNBBTC',
    u'price': u'0.00021087'
  },
  ...
  {
    u'symbol': u'DASHBTC',
    u'price': u'0.04872800'
  },
  {
    u'symbol': u'DASHETH',
    u'price': u'0.99112000'
  }
]
</pre>
</details>
	
####  Buy limit order
	binance.API_Post_BuyLimitOrder("SNTETH", 131, "0.00008111")
<details><summary>Show Output</summary>
<pre>
{
  u'orderId': 1866448,
  u'clientOrderId': u'e6NxhMuCxnqUtVJ2AfKkuV',
  u'origQty': u'131.00000000',
  u'symbol': u'SNTETH',
  u'side': u'BUY',
  u'timeInForce': u'GTC',
  u'status': u'NEW',
  u'transactTime': 1508458538408,
  u'type': u'LIMIT',
  u'price': u'0.00008111',
  u'executedQty': u'0.00000000'
}
</pre>
</details>
	
####  Sell limit order
	binance.API_Post_SellLimitOrder("SNTETH", 120, "0.00009049")
	
####  Buy market order
	binance.API_Post_BuyMarketOrder("SNTETH", 30)
	
####  Sell market order
	binance.API_Post_SellMarketOrder("SNTETH", 50)

####  Buy limit iceberg order
	binance.API_Post_BuyLimitOrder("ETHBTC", 0.01, "0.054", 0.0025)
	
####  Sell market iceberg order
	binance.API_Post_SellMarketOrder("ETHBTC", 0.01, 0.0025)

####  Get the status of an order
	binance.API_Get_OrderStatus("SNTETH", "1866448")
<details><summary>Show Output</summary>
<pre>
{
  u'orderId': 1866448,
  u'clientOrderId': u'e6NxhMuCxnqUtVJ2AfKkuV',
  u'origQty': u'131.00000000',
  u'icebergQty': u'0.00000000',
  u'symbol': u'SNTETH',
  u'side': u'BUY',
  u'timeInForce': u'GTC',
  u'status': u'NEW',
  u'stopPrice': u'0.00000000',
  u'time': 1508458538408,
  u'type': u'LIMIT',
  u'price': u'0.00008111',
  u'executedQty': u'0.00000000'
}
</pre>
</details>

####  Delete an open order
	binance.API_Delete_Order("SNTETH", "1866448")
<details><summary>Show Output</summary>
<pre>
{
  u'orderId': 1866448,
  u'clientOrderId': u'IpNsmi8RPaYcXXDXjxoscN',
  u'symbol': u'SNTETH',
  u'origClientOrderId': u'e6NxhMuCxnqUtVJ2AfKkuV'
}
</pre>
</details>
	
####  Get open orders
	# All open orders
	openOrders = binance.API_Get_OpenOrders("BNBETH")
	# Only open buy orders
	openBuyOrders = binance.API_Get_OpenBuyOrders("BNBETH")
	# Only open sell orders
	openSellOrders = binance.API_Get_OpenSellOrders("BNBETH")
<details><summary>Show Output</summary>
<pre>
openOrders = 
[
  {
    u'orderId': 3989984,
    u'clientOrderId': u'XDX5uvT6EYXYSrqGVnFtf7',
    u'origQty': u'3.00000000',
    u'icebergQty': u'0.00000000',
    u'symbol': u'BNBETH',
    u'side': u'BUY',
    u'timeInForce': u'GTC',
    u'status': u'NEW',
    u'stopPrice': u'0.00000000',
    u'time': 1508518881879,
    u'type': u'LIMIT',
    u'price': u'0.00401189',
    u'executedQty': u'0.00000000'
  },
  {
    u'orderId': 3990000,
    u'clientOrderId': u'iptndGLiwz5PtLYtV39rlU',
    u'origQty': u'3.00000000',
    u'icebergQty': u'0.00000000',
    u'symbol': u'BNBETH',
    u'side': u'SELL',
    u'timeInForce': u'GTC',
    u'status': u'NEW',
    u'stopPrice': u'0.00000000',
    u'time': 1508518906583,
    u'type': u'LIMIT',
    u'price': u'0.00435000',
    u'executedQty': u'0.00000000'
  }
]
openBuyOrders = 
[
  {
    u'orderId': 3989984,
    u'clientOrderId': u'XDX5uvT6EYXYSrqGVnFtf7',
    u'origQty': u'3.00000000',
    u'icebergQty': u'0.00000000',
    u'symbol': u'BNBETH',
    u'side': u'BUY',
    u'timeInForce': u'GTC',
    u'status': u'NEW',
    u'stopPrice': u'0.00000000',
    u'time': 1508518881879,
    u'type': u'LIMIT',
    u'price': u'0.00401189',
    u'executedQty': u'0.00000000'
  }
]
openSellOrders = 
[
  {
    u'orderId': 3990000,
    u'clientOrderId': u'iptndGLiwz5PtLYtV39rlU',
    u'origQty': u'3.00000000',
    u'icebergQty': u'0.00000000',
    u'symbol': u'BNBETH',
    u'side': u'SELL',
    u'timeInForce': u'GTC',
    u'status': u'NEW',
    u'stopPrice': u'0.00000000',
    u'time': 1508518906583,
    u'type': u'LIMIT',
    u'price': u'0.00435000',
    u'executedQty': u'0.00000000'
  }
]
</pre>
</details>

####  Get trade history
	binance.API_Get_TradeHistory("SNTETH")
<details><summary>Show Output</summary>
<pre>
[
  {
    u'orderId': 1828341,
    u'isBuyer': True,
    u'price': u'0.00009044',
    u'isMaker': False,
    u'qty': u'120.00000000',
    u'commission': u'0.12000000',
    u'time': 1508399279948,
    u'commissionAsset': u'SNT',
    u'id': 386679,
    u'isBestMatch': True
  },
  {
    u'orderId': 1828394,
    u'isBuyer': False,
    u'price': u'0.00009049',
    u'isMaker': True,
    u'qty': u'120.00000000',
    u'commission': u'0.00001086',
    u'time': 1508399893085,
    u'commissionAsset': u'ETH',
    u'id': 386709,
    u'isBestMatch': True
  },
  ...
  {
    u'orderId': 1864829,
    u'isBuyer': True,
    u'price': u'0.00008924',
    u'isMaker': False,
    u'qty': u'30.00000000',
    u'commission': u'0.00031375',
    u'time': 1508454466271,
    u'commissionAsset': u'BNB',
    u'id': 389600,
    u'isBestMatch': True
  }
]
</pre>
</details>

####  Get 24 hour ticker price change stats
	binance.API_Get_24TickerPriceChange("SNTETH")
<details><summary>Show Output</summary>
<pre>
{
  u'count': 4415,
  u'bidQty': u'2266.00000000',
  u'prevClosePrice': u'0.00008707',
  u'askQty': u'2248.00000000',
  u'lastPrice': u'0.00008921',
  u'lowPrice': u'0.00008492',
  u'askPrice': u'0.00008919',
  u'lastQty': u'1100.00000000',
  u'priceChange': u'0.00000209',
  u'openPrice': u'0.00008712',
  u'volume': u'5667098.00000000',
  u'openTime': 1508434278315,
  u'bidPrice': u'0.00008826',
  u'closeTime': 1508520678315,
  u'firstId': 388691,
  u'quoteVolume': u'503.19794500',
  u'weightedAvgPrice': u'0.00008879',
  u'lastId': 393105,
  u'priceChangePercent': u'2.399',
  u'highPrice': u'0.00009099'
}
</pre>
</details>

####  Get Kline/Candlestick data given interval
	binance.API_Get_KlineCandlestick("SNTETH", "30m")
<details><summary>Show Output</summary>
<pre>
[
  [
    1507622400000,
    u'0.00007630',
    u'0.00007634',
    u'0.00007536',
    u'0.00007536',
    u'132768.00000000',
    1507624199999,
    u'10.10279036',
    105,
    u'44289.00000000',
    u'3.36611129',
    u'84154027.76520122'
  ],
  [
    1507624200000,
    u'0.00007541',
    u'0.00007633',
    u'0.00007511',
    u'0.00007613',
    u'110807.00000000',
    1507625999999,
    u'8.36855540',
    71,
    u'23849.00000000',
    u'1.81251704',
    u'84154127.76520122'
  ],
  ...
  [
    1508520600000,
    u'0.00008921',
    u'0.00008921',
    u'0.00008915',
    u'0.00008915',
    u'1811.00000000',
    1508522399999,
    u'0.16151665',
    3,
    u'1811.00000000',
    u'0.16151665',
    u'105328636.04955539'
  ]
]
</pre>
</details>

####  Get aggregate trades
	binance.API_Get_AggregateTrades("SNTETH")
<details><summary>Show Output</summary>
<pre>
[
  {
    u'a': 385889,
    u'f': 392591,
    u'M': True,
    u'm': True,
    u'l': 392591,
    u'q': u'6714.00000000',
    u'p': u'0.00008868',
    u'T': 1508511121096
  },
  {
    u'a': 385890,
    u'f': 392592,
    u'M': True,
    u'm': True,
    u'l': 392592,
    u'q': u'4769.00000000',
    u'p': u'0.00008867',
    u'T': 1508511121208
  },
  ...
  {
    u'a': 386388,
    u'f': 393107,
    u'M': True,
    u'm': True,
    u'l': 393107,
    u'q': u'1923.00000000',
    u'p': u'0.00008684',
    u'T': 1508520765652
  }
]
</pre>
</details>
	
####  Websockets
    websocket.enableTrace(True)

    # Choose which URL you'd like to subscribe to
    url = "wss://stream.binance.com:9443/ws/ethbtc@depth"
    ws = websocket.WebSocketApp(url, on_message = on_message, on_error = on_error, on_close = on_close)
    ws.on_open = on_open
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
<details><summary>Show Output</summary>
<pre>
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
</pre>
</details>

From here, you can update your UI or your program's behavior with this real-time data from websockets.

Note: this library generates a log file called "logfile" which helps you debug and track transactions.

####  Binance's API + Automation = Next Level Trading

![alt text](https://i.imgur.com/op04NW2.png)  ![alt text](https://i.imgur.com/yxtboiV.png)

"When my bot makes a trade, send my phone a notification and log it to a Google Drive spreadsheet."

Use the API_Post_Stringify call to automate logging to help you track profits, transactions, balances, etc. You can even connect other physical/digital services like Google Drive, phone notifications, Twitter, Facebook, etc. 
Here, i've connected my Google Drive spreadsheet and my iPhone/Android notifications. So everytime my bot makes a trade, it sends me a notification and logs it to Google Drive. I can use this to track profits and make sure it's running properly. 

	stringifyMakerURLgoesHere = "https://webhooks.stringify.com/v1/events/fEKBTcS1iCb3F99yGsNpV9svvetMzGwG/1/8a6e11d394fb9ac1af60b789d6e95537/TMSooXKVpJNRZ5choay3"
	API_Post_Stringify("Bought 100 BNB on Binance!", stringifyMakerURLgoesHere)

Set up a [Stringify account](https://www.stringify.com/) with your iOS or Android mobile device. You can download it in the App Store or Google Play. 

Next, import this flow: ["When my bot makes a trade, send my phone a notification and log it to a Google Drive spreadsheet."](https://app.stringify.com/flow/ebtuMIcbGogPxvr7Etlh)

![alt text](https://i.imgur.com/m8TSfvO.png)  ![alt text](https://i.imgur.com/vWiofnw.png)

Your Binance trading bot will be the trigger on the left. It will trigger this automation and pass a message to your phone notification and Google Drive thing on the right. The Maker thing on the left generates a URL to which the API_Post_Stringify method can make a REST request. You'll need to copy/paste that URL (which is unique to you) into your python code. 

![alt text](https://i.imgur.com/MssRmyy.png)  ![alt text](https://i.imgur.com/J5lRaCc.png)

The notification and Google Drive things get configured such that the data from the Binance bot gets sent to them. 

This will get your feet wet with automating your trading experience. With Binance's fast and detailed APIs combined with this python library, you have all the tools you need to trade and automate your cryptocurrency exchange experience.