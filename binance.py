#!/usr/bin/env python

__author__ = "Joey Zacherl"
__license__ = "MIT"
__version__ = "1.0.0"
__description__ = "Binance API integration"
__email__ = "Joey.Zacherl@gmail.com"

from loggingConfig import InitLogging, PrintAndLogError, PrintAndLog
import requests
import sys, traceback
import json
import hmac
import hashlib
import subprocess


APIKey_Binance = None
APISecret_Binance = None


URL_Binance_Base = "https://www.binance.com/api/"
RequestTimeout_seconds = 15


def SetAPIKey(key):
    global APIKey_Binance
    APIKey_Binance = key


def SetAPISecret(secret):
    global APISecret_Binance
    APISecret_Binance = secret


def GetBinanceSignature(totalParams):
    global APISecret_Binance
    print "APISecret_Binance = ", APISecret_Binance
    signature = hmac.new(APISecret_Binance, totalParams, hashlib.sha256).hexdigest()
    return signature


def GetBinanceHeader():
    global APIKey_Binance
    print "APIKey_Binance = ", APIKey_Binance
    headers_Binance = {'content-type': 'application/json', 'X-MBX-APIKEY': APIKey_Binance}
    PrintAndLog("headers_Binance = " + str(headers_Binance))
    return headers_Binance


def API_Get_Ping_Binance():
    url = URL_Binance_Base + "v1/ping"
    PrintAndLog("url = " + url)

    response = requests.get(url, timeout=RequestTimeout_seconds)
    if (response.ok):
        responseData = response.content
        jData = json.loads(responseData)

        PrintAndLog("API_Get_Ping_Binance jData = " + str(jData))
        return jData

    else:
        # If response code is not ok (200), print the resulting http error code with description
        response.raise_for_status()


def API_Get_Time_Binance():
    url = URL_Binance_Base + "v1/time"
    PrintAndLog("url = " + url)

    response = requests.get(url, timeout=RequestTimeout_seconds)
    if (response.ok):
        responseData = response.content
        jData = json.loads(responseData)

        PrintAndLog("API_Get_Time_Binance jData = " + str(jData))
        return jData

    else:
        # If response code is not ok (200), print the resulting http error code with description
        response.raise_for_status()


def API_Get_TopNOrders_Binance(symbol, n, side):
    if side.lower() != "bids" and side.lower() != "asks" and side.lower() != "both":
        raise ValueError('side must be either bids, asks, or both')

    else:
        ordersJData = API_Get_Orders_Binance(symbol)
        # PrintAndLog("type(ordersJData) = " + str(type(ordersJData)))
        # PrintAndLog("type(ordersJData['bids']) = " + str(type(ordersJData['bids'])))
        # PrintAndLog("type(ordersJData['asks']) = " + str(type(ordersJData['asks'])))

        if side.lower() == "bids":
            returnList = ordersJData['bids'][:n]

        elif side.lower() == "asks":
            returnList = ordersJData['asks'][:n]

        elif side.lower() == "both":
            returnList = (ordersJData['bids'][:n], ordersJData['asks'][:n])

        # PrintAndLog("API_Get_TopNOrders_Binance returnList = " + str(returnList))
        return returnList


def API_Get_Orders_Binance(symbol):
    url = URL_Binance_Base + "v1/depth?symbol=" + str(symbol)
    PrintAndLog("url = " + url)
    # headers_local = {'content-type': 'application/json'}

    # response = requests.get(url, headers=headers_local, timeout=RequestTimeout_seconds)
    response = requests.get(url, timeout=RequestTimeout_seconds)
    if (response.ok):
        responseData = response.content
        jData = json.loads(responseData)

        # PrintAndLog("API_Get_Orders_Binance jData = " + str(jData))
        return jData

    else:
        # If response code is not ok (200), print the resulting http error code with description
        response.raise_for_status()


def API_Get_Price_Binance(symbol):
    marketsJData = API_Get_Markets_Binance()

    for market in marketsJData:
        firstFew = market['symbol'][:len(symbol)]

        # PrintAndLog("market = " + str(market) + " and firstFew = " + firstFew)
        if firstFew.lower() == symbol.lower():
            return market


def API_Get_Markets_Binance():
    url = URL_Binance_Base + "v1/ticker/allPrices"
    PrintAndLog("url = " + url)
    # headers_local = {'content-type': 'application/json'}

    # response = requests.get(url, headers=headers_local, timeout=RequestTimeout_seconds)
    response = requests.get(url, timeout=RequestTimeout_seconds)
    if (response.ok):
        responseData = response.content
        jData = json.loads(responseData)

        # PrintAndLog("API_Get_Markets_Binance jData = " + str(jData))
        return jData

    else:
        # If response code is not ok (200), print the resulting http error code with description
        response.raise_for_status()


def API_Get_TradeHistory_Binance(symbol, recvWindow=5000):
    timeStamp = GetTimeStamp_Binance()
    totalParams = "symbol=" + symbol.upper() + "&recvWindow=" + str(recvWindow) + "&timestamp=" + timeStamp
    PrintAndLog("totalParams = " + totalParams)
    signature = GetBinanceSignature(totalParams)
    PrintAndLog("signature = " + signature)

    url = URL_Binance_Base + "v3/myTrades?" + totalParams + "&signature=" + signature
    PrintAndLog("url = " + url)

    response = requests.get(url, headers=GetBinanceHeader(), timeout=RequestTimeout_seconds)
    if (response.ok):
        responseData = response.content
        jData = json.loads(responseData)

        PrintAndLog("API_Get_TradeHistory_Binance jData = " + str(jData))
        return jData

    else:
        # If response code is not ok (200), print the resulting http error code with description
        PrintAndLog("response = " + str(response.content))
        response.raise_for_status()


def API_Get_24TickerPriceChange_Binance(symbol):
    url = URL_Binance_Base + "v1/ticker/24hr?symbol=" + str(symbol)
    PrintAndLog("url = " + url)

    response = requests.get(url, timeout=RequestTimeout_seconds)
    if (response.ok):
        responseData = response.content
        jData = json.loads(responseData)

        PrintAndLog("API_Get_24TickerPriceChange_Binance jData = " + str(jData))
        return jData

    else:
        # If response code is not ok (200), print the resulting http error code with description
        PrintAndLog("response = " + str(response.content))
        response.raise_for_status()


def API_Get_KlineCandlestick_Binance(symbol, interval):
    url = URL_Binance_Base + "v1/klines?symbol=" + str(symbol) + "&interval=" + str(interval)
    PrintAndLog("url = " + url)

    response = requests.get(url, timeout=RequestTimeout_seconds)
    if (response.ok):
        responseData = response.content
        jData = json.loads(responseData)

        PrintAndLog("API_Get_KlineCandlestick_Binance jData = " + str(jData))
        return jData

    else:
        # If response code is not ok (200), print the resulting http error code with description
        PrintAndLog("response = " + str(response.content))
        response.raise_for_status()


def API_Get_AggregateTrades_Binance(symbol, recvWindow=5000):
    url = URL_Binance_Base + "v1/aggTrades?symbol=" + str(symbol)

    PrintAndLog("url = " + url)

    response = requests.get(url, timeout=RequestTimeout_seconds)
    if (response.ok):
        responseData = response.content
        jData = json.loads(responseData)

        PrintAndLog("API_Get_AggregateTrades_Binance jData = " + str(jData))
        return jData

    else:
        #  If response code is not ok (200), print the resulting http error code with description
        PrintAndLog("response = " + str(response.content))
        response.raise_for_status()


def GetTimeStamp_Binance():
    # Get the timestamp in milliseconds
    timeStamp = str(long(subprocess.check_output("gdate +%s%3N", shell=True)))
    return timeStamp


def API_Post_BuyLimitOrder_Binance(symbol, quantity, price, icebergQty=None, stopPrice=None, recvWindow=5000):
    return API_Post_LimitOrder_Binance(symbol, "buy", quantity, price, icebergQty, stopPrice, recvWindow)

def API_Post_SellLimitOrder_Binance(symbol, quantity, price, icebergQty=None, stopPrice=None, recvWindow=5000):
    return API_Post_LimitOrder_Binance(symbol, "sell", quantity, price, icebergQty, stopPrice, recvWindow)

def API_Post_LimitOrder_Binance(symbol, side, quantity, priceString, icebergQty, stopPrice, recvWindow):
    timeStamp = GetTimeStamp_Binance()

    if side.lower() == "buy" or side.lower() == "sell":
        side = side.upper()

    else:
        raise ValueError('side must be either buy or sell')

    totalParams = "symbol=" + symbol.upper() + "&side=" + side + "&type=LIMIT&timeInForce=GTC&quantity=" + str(quantity) + "&price=" + priceString + "&recvWindow=" + str(recvWindow) + "&timestamp=" + timeStamp

    if icebergQty:
        totalParams += "&icebergQty=" + str(icebergQty)

    if stopPrice:
        totalParams += "&stopPrice=" + str(stopPrice)

    PrintAndLog("totalParams = " + totalParams)
    signature = GetBinanceSignature(totalParams)
    PrintAndLog("signature = " + signature)

    url = URL_Binance_Base + "v3/order?" + totalParams + "&signature=" + signature
    PrintAndLog("url = " + url)

    response = requests.post(url, headers=GetBinanceHeader(), timeout=RequestTimeout_seconds)
    if (response.ok):
        responseData = response.content
        jData = json.loads(responseData)

        PrintAndLog("API_Post_LimitOrder_Binance jData = " + str(jData))
        return jData

    else:
        # If response code is not ok (200), print the resulting http error code with description
        PrintAndLog("response = " + str(response.content))
        response.raise_for_status()


def API_Post_BuyMarketOrder_Binance(symbol, quantity, icebergQty=None, stopPrice=None, recvWindow=5000):
    return API_Post_MarketOrder_Binance(symbol, "buy", quantity, icebergQty, stopPrice, recvWindow)

def API_Post_SellMarketOrder_Binance(symbol, quantity, icebergQty=None, stopPrice=None, recvWindow=5000):
    return API_Post_MarketOrder_Binance(symbol, "sell", quantity, icebergQty, stopPrice, recvWindow)

def API_Post_MarketOrder_Binance(symbol, side, quantity, icebergQty, stopPrice, recvWindow):
    timeStamp = GetTimeStamp_Binance()

    if side.lower() == "buy" or side.lower() == "sell":
        side = side.upper()

    else:
        raise ValueError('side must be either buy or sell')

    totalParams = "symbol=" + symbol.upper() + "&side=" + side + "&type=MARKET&quantity=" + str(quantity) + "&recvWindow=" + str(recvWindow) + "&timestamp=" + timeStamp

    if icebergQty:
        totalParams += "&icebergQty=" + str(icebergQty)

    if stopPrice:
        totalParams += "&stopPrice=" + str(stopPrice)

    PrintAndLog("totalParams = " + totalParams)
    signature = GetBinanceSignature(totalParams)
    PrintAndLog("signature = " + signature)

    url = URL_Binance_Base + "v3/order?" + totalParams + "&signature=" + signature
    PrintAndLog("url = " + url)

    response = requests.post(url, headers=GetBinanceHeader(), timeout=RequestTimeout_seconds)
    if (response.ok):
        responseData = response.content
        jData = json.loads(responseData)

        PrintAndLog("API_Post_MarketOrder_Binance jData = " + str(jData))
        return jData

    else:
        # If response code is not ok (200), print the resulting http error code with description
        PrintAndLog("response = " + str(response.content))
        response.raise_for_status()


def API_Get_OrderStatus_Binance(symbol, orderId, recvWindow=5000):
    timeStamp = GetTimeStamp_Binance()
    totalParams = "symbol=" + symbol.upper() + "&orderId=" + str(orderId) + "&recvWindow=" + str(recvWindow) + "&timestamp=" + timeStamp
    PrintAndLog("totalParams = " + totalParams)
    signature = GetBinanceSignature(totalParams)
    PrintAndLog("signature = " + signature)

    url = URL_Binance_Base + "v3/order?" + totalParams + "&signature=" + signature
    PrintAndLog("url = " + url)

    response = requests.get(url, headers=GetBinanceHeader(), timeout=RequestTimeout_seconds)
    if (response.ok):
        responseData = response.content
        jData = json.loads(responseData)

        PrintAndLog("API_Get_OrderStatus_Binance jData = " + str(jData))
        return jData

    else:
        # If response code is not ok (200), print the resulting http error code with description
        PrintAndLog("response = " + str(response.content))
        response.raise_for_status()


def API_Delete_Order_Binance(symbol, orderId, recvWindow=5000):
    timeStamp = GetTimeStamp_Binance()
    totalParams = "symbol=" + symbol.upper() + "&orderId=" + str(orderId) + "&recvWindow=" + str(recvWindow) + "&timestamp=" + timeStamp
    PrintAndLog("totalParams = " + totalParams)
    signature = GetBinanceSignature(totalParams)
    PrintAndLog("signature = " + signature)

    url = URL_Binance_Base + "v3/order?" + totalParams + "&signature=" + signature
    PrintAndLog("url = " + url)

    response = requests.delete(url, headers=GetBinanceHeader(), timeout=RequestTimeout_seconds)
    if (response.ok):
        responseData = response.content
        jData = json.loads(responseData)

        PrintAndLog("API_Delete_Order_Binance jData = " + str(jData))
        return jData

    else:
        # If response code is not ok (200), print the resulting http error code with description
        PrintAndLog("response = " + str(response.content))
        response.raise_for_status()


def API_Get_OpenOrders_Binance(symbol, recvWindow=5000):
    timeStamp = GetTimeStamp_Binance()
    totalParams = "symbol=" + symbol.upper() + "&recvWindow=" + str(recvWindow) + "&timestamp=" + timeStamp
    PrintAndLog("totalParams = " + totalParams)
    signature = GetBinanceSignature(totalParams)
    PrintAndLog("signature = " + signature)

    url = URL_Binance_Base + "v3/openOrders?" + totalParams + "&signature=" + signature
    PrintAndLog("url = " + url)

    response = requests.get(url, headers=GetBinanceHeader(), timeout=RequestTimeout_seconds)
    if (response.ok):
        responseData = response.content
        jData = json.loads(responseData)

        PrintAndLog("API_Get_OpenOrders_Binance jData = " + str(jData))
        return jData

    else:
        # If response code is not ok (200), print the resulting http error code with description
        PrintAndLog("response = " + str(response.content))
        response.raise_for_status()


def API_Get_Balance_Binance(currency):
    accountJData = API_Get_AccountInfo_Binance()

    for balance in accountJData['balances']:
        if currency.lower() == balance['asset'].lower():
            return balance


def API_Get_AccountInfo_Binance(recvWindow=5000):
    timeStamp = GetTimeStamp_Binance()
    totalParams = "recvWindow=" + str(recvWindow) + "&timestamp=" + timeStamp
    PrintAndLog("totalParams = " + totalParams)
    signature = GetBinanceSignature(totalParams)
    PrintAndLog("signature = " + signature)

    url = URL_Binance_Base + "v3/account?" + totalParams + "&signature=" + signature
    PrintAndLog("url = " + url)

    response = requests.get(url, headers=GetBinanceHeader(), timeout=RequestTimeout_seconds)
    if (response.ok):
        responseData = response.content
        jData = json.loads(responseData)

        # PrintAndLog("API_Get_AccountInfo_Binance jData = " + str(jData))
        return jData

    else:
        # If response code is not ok (200), print the resulting http error code with description
        PrintAndLog("response = " + str(response.content))
        response.raise_for_status()

