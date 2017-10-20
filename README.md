# Binance Python API integration

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
	
####  Get orders for a symbol
	binance.API_Get_Orders_Binance("BNBETH")
	
####  Get the top n bids and/or asks for a symbol
	topNBids = binance.API_Get_TopNOrders_Binance("BNBETH", 10, "bids")
	topNAsks = binance.API_Get_TopNOrders_Binance("BNBETH", 10, "asks")
	topNBids, topNAsks = binance.API_Get_TopNOrders_Binance("BNBETH", 10, "both")

####  Get account info, free/locked balances, etc
	info = binance.API_Get_AccountInfo_Binance()
	
	# or get one at a time
	balance_bnb = binance.API_Get_Balance_Binance("bnb")
	balance_eth = binance.API_Get_Balance_Binance("eth")
	# Sample output: balance_eos = {u'locked': u'0.00000000', u'asset': u'BNB', u'free': u'2.99593206'}
	# Sample output: balance_eth = {u'locked': u'0.00000000', u'asset': u'ETH', u'free': u'0.03479956'}

I, Joey Zacherl, fully own the code I submit.  I guarantee there are no copyright or license restrictions.  I further agree any code I submit will be in public domain.  Anyone can copy, change, derive further work from it without any restrictions.