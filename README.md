# Python Binance API integration

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
	
#### Ping and server time
	# Ping the API
	binance.API_Get_Ping_Binance()
	# Get current Time
	binance.API_Get_Time_Binance()
<details><summary>Show Output</summary>
<pre>
{}
{u'serverTime': 1508517204492}
</pre>
</details>
	
#### Get orders for a symbol
	orders = binance.API_Get_Orders_Binance("BNBETH")
<details><summary>Show Output</summary>
<pre>
{u'lastUpdateId': 6602561, u'bids': [[u'0.00406001', u'36.00000000', []], [u'0.00406000', u'89.00000000', []], [u'0.00405108', u'312.00000000', []], [u'0.00405106', u'449.00000000', []], [u'0.00405100', u'330.00000000', []], [u'0.00405001', u'729.00000000', []], [u'0.00405000', u'4241.00000000', []], [u'0.00404017', u'840.00000000', []], [u'0.00404000', u'183.00000000', []], [u'0.00403004', u'1391.00000000', []], [u'0.00403000', u'87.00000000', []], [u'0.00402614', u'7213.00000000', []], [u'0.00402613', u'196.00000000', []], [u'0.00402320', u'1000.00000000', []], [u'0.00402300', u'267.00000000', []], [u'0.00402123', u'301.00000000', []], [u'0.00402120', u'25.00000000', []], [u'0.00402000', u'1080.00000000', []], [u'0.00401500', u'100.00000000', []], [u'0.00401189', u'251.00000000', []], [u'0.00401188', u'74777.00000000', []], [u'0.00401067', u'498.00000000', []], [u'0.00401000', u'66.00000000', []], [u'0.00400800', u'100.00000000', []], [u'0.00400100', u'153.00000000', []], [u'0.00400090', u'1800.00000000', []], [u'0.00400003', u'500.00000000', []], [u'0.00400001', u'550.00000000', []], [u'0.00400000', u'73389.00000000', []], [u'0.00398080', u'100.00000000', []], [u'0.00398000', u'40.00000000', []], [u'0.00396000', u'240.00000000', []], [u'0.00395141', u'18.00000000', []], [u'0.00394000', u'140.00000000', []], [u'0.00391040', u'30.00000000', []], [u'0.00391000', u'200.00000000', []], [u'0.00390100', u'50.00000000', []], [u'0.00390000', u'2617.00000000', []], [u'0.00388930', u'88.00000000', []], [u'0.00388880', u'166.00000000', []], [u'0.00388000', u'138.00000000', []], [u'0.00387800', u'165.00000000', []], [u'0.00387000', u'5167.00000000', []], [u'0.00386420', u'894.00000000', []], [u'0.00385551', u'3073.00000000', []], [u'0.00385378', u'30.00000000', []], [u'0.00385300', u'139.00000000', []], [u'0.00385000', u'1654.00000000', []], [u'0.00382117', u'20.00000000', []], [u'0.00382000', u'500.00000000', []], [u'0.00381447', u'985.00000000', []], [u'0.00381420', u'35.00000000', []], [u'0.00381020', u'1000.00000000', []], [u'0.00380000', u'3929.00000000', []], [u'0.00378800', u'70.00000000', []], [u'0.00377778', u'212.00000000', []], [u'0.00377777', u'49.00000000', []], [u'0.00377100', u'65.00000000', []], [u'0.00377030', u'534.00000000', []], [u'0.00375000', u'215.00000000', []], [u'0.00373737', u'1546.00000000', []], [u'0.00373200', u'145.00000000', []], [u'0.00372580', u'250.00000000', []], [u'0.00370300', u'24.00000000', []], [u'0.00370000', u'2728.00000000', []], [u'0.00366666', u'520.00000000', []], [u'0.00366600', u'1874.00000000', []], [u'0.00364200', u'12.00000000', []], [u'0.00364000', u'1290.00000000', []], [u'0.00363457', u'912.00000000', []], [u'0.00361000', u'810.00000000', []], [u'0.00360800', u'203.00000000', []], [u'0.00360449', u'39.00000000', []], [u'0.00360000', u'1132.00000000', []], [u'0.00358880', u'25.00000000', []], [u'0.00358443', u'732.00000000', []], [u'0.00355280', u'141.00000000', []], [u'0.00354450', u'268.00000000', []], [u'0.00350200', u'200.00000000', []], [u'0.00350020', u'10.00000000', []], [u'0.00350000', u'5033.00000000', []], [u'0.00349000', u'1113.00000000', []], [u'0.00345000', u'150.00000000', []], [u'0.00343000', u'153.00000000', []], [u'0.00341100', u'3000.00000000', []], [u'0.00341000', u'442.00000000', []], [u'0.00335916', u'10.00000000', []], [u'0.00335000', u'4.00000000', []], [u'0.00334894', u'534.00000000', []], [u'0.00333334', u'3.00000000', []], [u'0.00330000', u'426.00000000', []], [u'0.00329000', u'885.00000000', []], [u'0.00328900', u'488.00000000', []], [u'0.00328000', u'100.00000000', []], [u'0.00324249', u'50.00000000', []], [u'0.00320939', u'45.00000000', []], [u'0.00320000', u'394.00000000', []], [u'0.00318719', u'594.00000000', []], [u'0.00312400', u'130.00000000', []], [u'0.00311100', u'165.00000000', []]], u'asks': [[u'0.00410516', u'298.00000000', []], [u'0.00410517', u'200.00000000', []], [u'0.00410879', u'2000.00000000', []], [u'0.00410880', u'1040.00000000', []], [u'0.00414750', u'375.00000000', []], [u'0.00414874', u'1000.00000000', []], [u'0.00414999', u'4481.00000000', []], [u'0.00415000', u'20.00000000', []], [u'0.00418495', u'825.00000000', []], [u'0.00418500', u'5.00000000', []], [u'0.00419000', u'392.00000000', []], [u'0.00420000', u'200.00000000', []], [u'0.00421000', u'600.00000000', []], [u'0.00421292', u'21.00000000', []], [u'0.00423252', u'1062.00000000', []], [u'0.00425000', u'320.00000000', []], [u'0.00426170', u'16.00000000', []], [u'0.00426686', u'260.00000000', []], [u'0.00426695', u'260.00000000', []], [u'0.00428671', u'48.00000000', []], [u'0.00435000', u'39.00000000', []], [u'0.00437507', u'264.00000000', []], [u'0.00438910', u'95.00000000', []], [u'0.00439713', u'358.00000000', []], [u'0.00439846', u'716.00000000', []], [u'0.00439900', u'1100.00000000', []], [u'0.00440000', u'413.00000000', []], [u'0.00440005', u'65.00000000', []], [u'0.00440100', u'1000.00000000', []], [u'0.00440131', u'35.00000000', []], [u'0.00440990', u'1432.00000000', []], [u'0.00441000', u'500.00000000', []], [u'0.00441250', u'120.00000000', []], [u'0.00441600', u'1728.00000000', []], [u'0.00441971', u'359.00000000', []], [u'0.00441998', u'948.00000000', []], [u'0.00442861', u'936.00000000', []], [u'0.00443300', u'3.00000000', []], [u'0.00444444', u'1406.00000000', []], [u'0.00445000', u'412.00000000', []], [u'0.00446000', u'167.00000000', []], [u'0.00446703', u'264.00000000', []], [u'0.00448000', u'200.00000000', []], [u'0.00448894', u'2700.00000000', []], [u'0.00449124', u'100.00000000', []], [u'0.00449800', u'221.00000000', []], [u'0.00449998', u'3.00000000', []], [u'0.00450000', u'3339.00000000', []], [u'0.00451630', u'858.00000000', []], [u'0.00452220', u'3549.00000000', []], [u'0.00452800', u'75.00000000', []], [u'0.00454000', u'55.00000000', []], [u'0.00455555', u'1875.00000000', []], [u'0.00457500', u'1.00000000', []], [u'0.00458000', u'100.00000000', []], [u'0.00458100', u'13.00000000', []], [u'0.00459000', u'300.00000000', []], [u'0.00459990', u'18750.00000000', []], [u'0.00460000', u'5131.00000000', []], [u'0.00460500', u'50.00000000', []], [u'0.00460619', u'781.00000000', []], [u'0.00461000', u'40.00000000', []], [u'0.00463014', u'20.00000000', []], [u'0.00465000', u'100.00000000', []], [u'0.00465400', u'473.00000000', []], [u'0.00465500', u'130.00000000', []], [u'0.00465870', u'372.00000000', []], [u'0.00465876', u'500.00000000', []], [u'0.00466235', u'800.00000000', []], [u'0.00466666', u'2500.00000000', []], [u'0.00468000', u'100.00000000', []], [u'0.00468800', u'1500.00000000', []], [u'0.00468888', u'11888.00000000', []], [u'0.00469800', u'137.00000000', []], [u'0.00469900', u'1000.00000000', []], [u'0.00469998', u'170.00000000', []], [u'0.00470000', u'1863.00000000', []], [u'0.00470511', u'20.00000000', []], [u'0.00471300', u'62.00000000', []], [u'0.00471888', u'6888.00000000', []], [u'0.00473124', u'3000.00000000', []], [u'0.00474003', u'180.00000000', []], [u'0.00475288', u'3.00000000', []], [u'0.00476000', u'236.00000000', []], [u'0.00477000', u'24.00000000', []], [u'0.00478000', u'290.00000000', []], [u'0.00478100', u'9.00000000', []], [u'0.00478200', u'523.00000000', []], [u'0.00479000', u'8000.00000000', []], [u'0.00479100', u'2000.00000000', []], [u'0.00479300', u'591.00000000', []], [u'0.00479900', u'1257.00000000', []], [u'0.00480000', u'3559.00000000', []], [u'0.00480050', u'44.00000000', []], [u'0.00481000', u'1059.00000000', []], [u'0.00482000', u'2371.00000000', []], [u'0.00483000', u'19.00000000', []], [u'0.00484900', u'2000.00000000', []], [u'0.00484980', u'765.00000000', []], [u'0.00484999', u'1000.00000000', []]]}
</pre>
</details>
	
####  Get the top n bids and/or asks for a symbol
	# Get to 10 in separate calls
	topNBids = binance.API_Get_TopNOrders_Binance("BNBETH", 10, "bids")
	topNAsks = binance.API_Get_TopNOrders_Binance("BNBETH", 10, "asks")
	# Get top 10 in one single call
	topNBids, topNAsks = binance.API_Get_TopNOrders_Binance("BNBETH", 10, "both")
<details><summary>Show Output</summary>
<pre>
topNBids = [[u'0.00410000', u'10.00000000', []], [u'0.00406006', u'100.00000000', []], [u'0.00405110', u'300.00000000', []], [u'0.00405108', u'312.00000000', []], [u'0.00405106', u'449.00000000', []], [u'0.00405100', u'330.00000000', []], [u'0.00405001', u'729.00000000', []], [u'0.00405000', u'4241.00000000', []], [u'0.00404019', u'1388.00000000', []], [u'0.00404017', u'840.00000000', []]]
topNAsks = [[u'0.00410829', u'2000.00000000', []], [u'0.00410830', u'324.00000000', []], [u'0.00410837', u'200.00000000', []], [u'0.00410880', u'1040.00000000', []], [u'0.00414750', u'375.00000000', []], [u'0.00414874', u'1000.00000000', []], [u'0.00414999', u'4480.00000000', []], [u'0.00415000', u'20.00000000', []], [u'0.00418500', u'5.00000000', []], [u'0.00418999', u'825.00000000', []]]
</pre>
</details>

####  Get account info, free/locked balances, etc
	# Get all account info
	allInfo = binance.API_Get_AccountInfo_Binance()
	# Or get only asset balances for one symbol at a time
	balance_bnb = binance.API_Get_Balance_Binance("bnb")
	balance_eth = binance.API_Get_Balance_Binance("eth")
<details><summary>Show Output</summary>
<pre>
allInfo = {u'buyerCommission': 0, u'canWithdraw': True, u'takerCommission': 10, u'canTrade': True, u'makerCommission': 10, u'balances': [{u'locked': u'0.00000000', u'asset': u'BTC', u'free': u'0.00053875'}, {u'locked': u'0.00000000', u'asset': u'LTC', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'ETH', u'free': u'0.03479956'}, {u'locked': u'0.00000000', u'asset': u'BNC', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'ICO', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'NEO', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'BNB', u'free': u'22.99593206'}, {u'locked': u'0.00000000', u'asset': u'123', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'456', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'QTUM', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'EOS', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'SNT', u'free': u'35.08000000'}, {u'locked': u'0.00000000', u'asset': u'BNT', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'GAS', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'BCC', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'BTM', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'USDT', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'HCC', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'HSR', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'OAX', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'DNT', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'MCO', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'ICN', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'ELC', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'PAY', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'ZRX', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'OMG', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'WTC', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'LRX', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'YOYO', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'LRC', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'LLT', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'TRX', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'FID', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'SNGLS', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'STRAT', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'BQX', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'FUN', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'KNC', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'CDT', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'XVG', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'IOTA', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'SNM', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'LINK', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'CVC', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'TNT', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'REP', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'CTR', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'MDA', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'MTL', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'SALT', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'NULS', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'SUB', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'STX', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'MTH', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'CAT', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'ADX', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'PIX', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'ETC', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'ENG', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'ZEC', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'AST', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'1ST', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'GNT', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'DGD', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'BAT', u'free': u'0.00000000'}, {u'locked': u'0.00000000', u'asset': u'DASH', u'free': u'0.00000000'}], u'sellerCommission': 0, u'canDeposit': True}
balance_bnb = {u'locked': u'0.00000000', u'asset': u'BNB', u'free': u'2.99593206'}
balance_eth = {u'locked': u'0.00000000', u'asset': u'ETH', u'free': u'0.03479956'}
</pre>
</details>
	
####  Get prices
	# All at once
	markets = binance.API_Get_Markets_Binance()
	# One at a time
	BNB = binance.API_Get_Price_Binance("BNB")
<details><summary>Show Output</summary>
<pre>
markets = [{u'symbol': u'ETHBTC', u'price': u'0.05126100'}, {u'symbol': u'LTCBTC', u'price': u'0.01018100'}, {u'symbol': u'BNBBTC', u'price': u'0.00021087'}, {u'symbol': u'NEOBTC', u'price': u'0.00476200'}, {u'symbol': u'123456', u'price': u'0.00030000'}, {u'symbol': u'QTUMETH', u'price': u'0.03799200'}, {u'symbol': u'EOSETH', u'price': u'0.00178600'}, {u'symbol': u'SNTETH', u'price': u'0.00008958'}, {u'symbol': u'BNTETH', u'price': u'0.00699300'}, {u'symbol': u'BCCBTC', u'price': u'0.05519800'}, {u'symbol': u'GASBTC', u'price': u'0.00332300'}, {u'symbol': u'BNBETH', u'price': u'0.00410667'}, {u'symbol': u'BTMETH', u'price': u'0.00018900'}, {u'symbol': u'HCCBTC', u'price': u'0.00000180'}, {u'symbol': u'BTCUSDT', u'price': u'5940.07000000'}, {u'symbol': u'ETHUSDT', u'price': u'304.02000000'}, {u'symbol': u'HSRBTC', u'price': u'0.00289000'}, {u'symbol': u'OAXETH', u'price': u'0.00130000'}, {u'symbol': u'DNTETH', u'price': u'0.00019104'}, {u'symbol': u'MCOETH', u'price': u'0.02399000'}, {u'symbol': u'ICNETH', u'price': u'0.00400000'}, {u'symbol': u'ELCBTC', u'price': u'0.00000053'}, {u'symbol': u'MCOBTC', u'price': u'0.00125800'}, {u'symbol': u'WTCBTC', u'price': u'0.00107000'}, {u'symbol': u'WTCETH', u'price': u'0.02087700'}, {u'symbol': u'LLTBTC', u'price': u'0.00001669'}, {u'symbol': u'LRCBTC', u'price': u'0.00001100'}, {u'symbol': u'LRCETH', u'price': u'0.00016311'}, {u'symbol': u'QTUMBTC', u'price': u'0.00192900'}, {u'symbol': u'YOYOBTC', u'price': u'0.00000481'}, {u'symbol': u'OMGBTC', u'price': u'0.00126800'}, {u'symbol': u'OMGETH', u'price': u'0.02503300'}, {u'symbol': u'ZRXBTC', u'price': u'0.00003547'}, {u'symbol': u'ZRXETH', u'price': u'0.00069300'}, {u'symbol': u'STRATBTC', u'price': u'0.00051500'}, {u'symbol': u'STRATETH', u'price': u'0.01021600'}, {u'symbol': u'SNGLSBTC', u'price': u'0.00002492'}, {u'symbol': u'SNGLSETH', u'price': u'0.00048705'}, {u'symbol': u'BQXBTC', u'price': u'0.00011803'}, {u'symbol': u'BQXETH', u'price': u'0.00230000'}, {u'symbol': u'KNCBTC', u'price': u'0.00017402'}, {u'symbol': u'KNCETH', u'price': u'0.00342600'}, {u'symbol': u'FUNBTC', u'price': u'0.00000340'}, {u'symbol': u'FUNETH', u'price': u'0.00006635'}, {u'symbol': u'SNMBTC', u'price': u'0.00001664'}, {u'symbol': u'SNMETH', u'price': u'0.00033072'}, {u'symbol': u'NEOETH', u'price': u'0.09309800'}, {u'symbol': u'IOTABTC', u'price': u'0.00006758'}, {u'symbol': u'IOTAETH', u'price': u'0.00132877'}, {u'symbol': u'LINKBTC', u'price': u'0.00004101'}, {u'symbol': u'LINKETH', u'price': u'0.00081757'}, {u'symbol': u'XVGBTC', u'price': u'0.00000074'}, {u'symbol': u'XVGETH', u'price': u'0.00001495'}, {u'symbol': u'CTRBTC', u'price': u'0.00009299'}, {u'symbol': u'CTRETH', u'price': u'0.00182230'}, {u'symbol': u'SALTBTC', u'price': u'0.00046700'}, {u'symbol': u'SALTETH', u'price': u'0.00910300'}, {u'symbol': u'MDABTC', u'price': u'0.00022621'}, {u'symbol': u'MDAETH', u'price': u'0.00448890'}, {u'symbol': u'MTLBTC', u'price': u'0.00119100'}, {u'symbol': u'MTLETH', u'price': u'0.02506700'}, {u'symbol': u'SUBBTC', u'price': u'0.00002220'}, {u'symbol': u'SUBETH', u'price': u'0.00043500'}, {u'symbol': u'EOSBTC', u'price': u'0.00009128'}, {u'symbol': u'SNTBTC', u'price': u'0.00000454'}, {u'symbol': u'ETC', u'price': u'0.00000000'}, {u'symbol': u'ETCETH', u'price': u'0.03742700'}, {u'symbol': u'ETCBTC', u'price': u'0.00188900'}, {u'symbol': u'MTHBTC', u'price': u'0.00001255'}, {u'symbol': u'MTHETH', u'price': u'0.00023999'}, {u'symbol': u'ENGBTC', u'price': u'0.00007112'}, {u'symbol': u'ENGETH', u'price': u'0.00140000'}, {u'symbol': u'DNTBTC', u'price': u'0.00000991'}, {u'symbol': u'ZECBTC', u'price': u'0.00000000'}, {u'symbol': u'ZECETH', u'price': u'0.00000000'}, {u'symbol': u'BNTBTC', u'price': u'0.00034198'}, {u'symbol': u'ASTBTC', u'price': u'0.00004615'}, {u'symbol': u'ASTETH', u'price': u'0.00090010'}, {u'symbol': u'DASHBTC', u'price': u'0.04872800'}, {u'symbol': u'DASHETH', u'price': u'0.99112000'}]
BNB = {u'symbol': u'BNBBTC', u'price': u'0.00021087'}
</pre>
</details>
	
####  Buy limit order
	binance.API_Post_BuyLimitOrder_Binance("SNTETH", 131, "0.00008111")
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
	binance.API_Delete_Order_Binance("SNTETH", "1866448")
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
	openOrders = binance.API_Get_OpenOrders_Binance("BNBETH")
<details><summary>Show Output</summary>
<pre>
[{u'orderId': 3989984, u'clientOrderId': u'XDX5uvT6EYXYSrqGVnFtf7', u'origQty': u'3.00000000', u'icebergQty': u'0.00000000', u'symbol': u'BNBETH', u'side': u'BUY', u'timeInForce': u'GTC', u'status': u'NEW', u'stopPrice': u'0.00000000', u'time': 1508518881879, u'type': u'LIMIT', u'price': u'0.00401189', u'executedQty': u'0.00000000'}, {u'orderId': 3990000, u'clientOrderId': u'iptndGLiwz5PtLYtV39rlU', u'origQty': u'3.00000000', u'icebergQty': u'0.00000000', u'symbol': u'BNBETH', u'side': u'SELL', u'timeInForce': u'GTC', u'status': u'NEW', u'stopPrice': u'0.00000000', u'time': 1508518906583, u'type': u'LIMIT', u'price': u'0.00435000', u'executedQty': u'0.00000000'}]
openOrders = [{u'orderId': 3989984, u'clientOrderId': u'XDX5uvT6EYXYSrqGVnFtf7', u'origQty': u'3.00000000', u'icebergQty': u'0.00000000', u'symbol': u'BNBETH', u'side': u'BUY', u'timeInForce': u'GTC', u'status': u'NEW', u'stopPrice': u'0.00000000', u'time': 1508518881879, u'type': u'LIMIT', u'price': u'0.00401189', u'executedQty': u'0.00000000'}, {u'orderId': 3990000, u'clientOrderId': u'iptndGLiwz5PtLYtV39rlU', u'origQty': u'3.00000000', u'icebergQty': u'0.00000000', u'symbol': u'BNBETH', u'side': u'SELL', u'timeInForce': u'GTC', u'status': u'NEW', u'stopPrice': u'0.00000000', u'time': 1508518906583, u'type': u'LIMIT', u'price': u'0.00435000', u'executedQty': u'0.00000000'}]
</pre>
</details>

####  Get trade history
	binance.API_Get_TradeHistory_Binance("SNTETH")
<details><summary>Show Output</summary>
<pre>
[{u'orderId': 1828341, u'isBuyer': True, u'price': u'0.00009044', u'isMaker': False, u'qty': u'120.00000000', u'commission': u'0.12000000', u'time': 1508399279948, u'commissionAsset': u'SNT', u'id': 386679, u'isBestMatch': True}, {u'orderId': 1828394, u'isBuyer': False, u'price': u'0.00009049', u'isMaker': True, u'qty': u'120.00000000', u'commission': u'0.00001086', u'time': 1508399893085, u'commissionAsset': u'ETH', u'id': 386709, u'isBestMatch': True}, {u'orderId': 1858113, u'isBuyer': True, u'price': u'0.00008809', u'isMaker': False, u'qty': u'20.00000000', u'commission': u'0.00021319', u'time': 1508442943941, u'commissionAsset': u'BNB', u'id': 389115, u'isBestMatch': True}, {u'orderId': 1858157, u'isBuyer': True, u'price': u'0.00008801', u'isMaker': False, u'qty': u'30.00000000', u'commission': u'0.00031999', u'time': 1508443011531, u'commissionAsset': u'BNB', u'id': 389116, u'isBestMatch': True}, {u'orderId': 1858181, u'isBuyer': False, u'price': u'0.00008693', u'isMaker': False, u'qty': u'50.00000000', u'commission': u'0.00053085', u'time': 1508443048017, u'commissionAsset': u'BNB', u'id': 389120, u'isBestMatch': True}, {u'orderId': 1864829, u'isBuyer': True, u'price': u'0.00008924', u'isMaker': False, u'qty': u'30.00000000', u'commission': u'0.00031375', u'time': 1508454466271, u'commissionAsset': u'BNB', u'id': 389600, u'isBestMatch': True}]
</pre>
</details>

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