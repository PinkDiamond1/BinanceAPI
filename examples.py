#!/usr/bin/env python

__author__ = "Joey Zacherl"
__license__ = "MIT"
__version__ = "1.0.0"
__description__ = "Binance API integration"
__email__ = "Joey.Zacherl@gmail.com"

import binance
from loggingConfig import InitLogging, PrintAndLogError, PrintAndLog
import requests
import json
import sys, traceback
import time


# Make an API call to Stringify's Maker thing to automate your script
# https://search.stringify.com/things/fEKBTcS1iCb3F99yGsNpV9svvetMzGwG_1
def API_Post_Stringify(message, stringifyMakerUrl):
    try:
        data = message
        requests.post(stringifyMakerUrl, data=data, timeout=10)

    except:
        PrintAndLogError("Exception inside API_Post_Stringify: " + traceback.format_exc())
        pass


# Put your API Key and Secret here!
# binance.SetAPIKey("APIKeyGoesHere")
# binance.SetAPISecret("APISecretGoesHere")


# Ping the API
binance.API_Get_Ping_Binance()

# Get current Time
binance.API_Get_Time_Binance()

# TODO, Comment things in below as you'd like to test them

# Get orders for a symbol
# orders = binance.API_Get_Orders_Binance("BNBETH")
# PrintAndLog("orders = " + str(orders))

# Get the top n bid/ask orders for a symbol
topNBids = binance.API_Get_TopNOrders_Binance("BNBETH", 10, "bids")
topNAsks = binance.API_Get_TopNOrders_Binance("BNBETH", 10, "asks")
topNBids, topNAsks = binance.API_Get_TopNOrders_Binance("BNBETH", 10, "both")
PrintAndLog("topNBids = " + str(topNBids))
PrintAndLog("topNAsks = " + str(topNAsks))

# Get account info, free/locked balances, etc
# info = binance.API_Get_AccountInfo_Binance()
# PrintAndLog("info = " + str(info))

# Get free/locked balances for an asset
# balance_bnb = binance.API_Get_Balance_Binance("bnb")
# balance_eth = binance.API_Get_Balance_Binance("eth")
# PrintAndLog("balance_bnb = " + str(balance_bnb))
# PrintAndLog("balance_eth = " + str(balance_eth))

# Get all prices
# binance.API_Get_Markets_Binance()

# Get price
# BNB = binance.API_Get_Price_Binance("BNB")
# PrintAndLog("BNB = " + str(BNB))

# Buy limit order
# binance.API_Post_BuyLimitOrder_Binance("SNTETH", 131, "0.00008111")
# # Sell limit order
# binance.API_Post_SellLimitOrder_Binance("SNTETH", 120, "0.00009049")
# # Buy market order
# binance.API_Post_BuyMarketOrder_Binance("SNTETH", 30)
# # Sell market order
# binance.API_Post_SellMarketOrder_Binance("SNTETH", 50)
#
# # Buy limit iceberg order
# binance.API_Post_BuyLimitOrder_Binance("ETHBTC", 0.01, "0.054", 0.0025)
# # Sell market iceberg order
# binance.API_Post_SellMarketOrder_Binance("ETHBTC", 0.01, 0.0025)

# # Get the status of an order, given orderId
# binance.API_Get_OrderStatus_Binance("SNTETH", "1866448")
#
# # Delete an open order
# binance.API_Delete_Order_Binance("SNTETH", "1866448")

# Get open orders
# binance.API_Get_OpenOrders_Binance("SNTETH")

# Get order history
# binance.API_Get_TradeHistory_Binance("SNTETH")

# Get 24 hour ticker price change stats
# binance.API_Get_24TickerPriceChange_Binance("SNTETH")

# Get Kline/Candlestick data given interval: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M
# binance.API_Get_KlineCandlestick_Binance("SNTETH", "30m")

# Get aggregate trades
# binance.API_Get_AggregateTrades_Binance("SNTETH")


# Use the API_Post_Stringify call to automate logging to help you track profits, transactions, balances, etc all
# You can have your program/bot/whatever log your transactions and balances to Google Drive or send your iPhone/Android phone push notifications.
# Use Stringify to "connect" this program to anything: https://www.stringify.com/

# You'll want to replace these URLs with yours, ones to your Stringify thing you created in your flow
# Here is a sample flow with google drive and notifications: https://app.stringify.com/flow/ebtuMIcbGogPxvr7Etlh
# Here is a sample flow with just google drive: https://app.stringify.com/flow/Nm3042oINKEkylVFmhMa
# API_Post_Stringify("Testing Phone", "https://webhooks.stringify.com/v1/events/fEKBTcS1iCb3F99yGsNpV9svvetMzGwG/1/8a6e11d394fb9ac1af60b789d6e95537/TMSooXKVpJNRZ5choay3")
# time.sleep(10)
# API_Post_Stringify("Testing Google Drive", "https://webhooks.stringify.com/v1/events/fEKBTcS1iCb3F99yGsNpV9svvetMzGwG/1/8a6e11d394fb9ac1af60b789d6e95537/XqPMuenh0j7T9DFsq0UR")
# time.sleep(10)
# API_Post_Stringify("Bought 100 BNB on Binance!", "https://webhooks.stringify.com/v1/events/fEKBTcS1iCb3F99yGsNpV9svvetMzGwG/1/8a6e11d394fb9ac1af60b789d6e95537/EKtASWus12uPJvEYV4pR")

