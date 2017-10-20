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
import time


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


def IsAPIKeySecretSet():
    global APIKey_Binance
    global APISecret_Binance

    if APIKey_Binance and APISecret_Binance:
        return True

    else:
        return False


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


def API_Get_Ping():
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


def API_Get_Time():
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


def API_Get_TopNOrders(symbol, n, side):
    if side.lower() != "bids" and side.lower() != "asks" and side.lower() != "both":
        raise ValueError('side must be either bids, asks, or both')

    else:
        ordersJData = API_Get_Orders(symbol)
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


def API_Get_Orders(symbol):
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


def API_Get_Price(symbol):
    marketsJData = API_Get_Markets()

    for market in marketsJData:
        firstFew = market['symbol'][:len(symbol)]

        # PrintAndLog("market = " + str(market) + " and firstFew = " + firstFew)
        if firstFew.lower() == symbol.lower():
            return market


def API_Get_Markets():
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


def API_Get_TradeHistory(symbol, recvWindow=5000):
    if not IsAPIKeySecretSet():
        raise Exception('API Key or Secret is not set. Set that before making this call.')

    timeStamp = GetTimeStamp()
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


def API_Get_24TickerPriceChange(symbol):
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


def API_Get_KlineCandlestick(symbol, interval):
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


def API_Get_AggregateTrades(symbol, recvWindow=5000):
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


def GetTimeStamp():
    timeStamp = str(long(round(time.time() * 1000)))
    return timeStamp


def API_Post_BuyLimitOrder(symbol, quantity, price, icebergQty=None, stopPrice=None, recvWindow=5000):
    return API_Post_LimitOrder(symbol, "buy", quantity, price, icebergQty, stopPrice, recvWindow)

def API_Post_SellLimitOrder(symbol, quantity, price, icebergQty=None, stopPrice=None, recvWindow=5000):
    return API_Post_LimitOrder(symbol, "sell", quantity, price, icebergQty, stopPrice, recvWindow)

def API_Post_LimitOrder(symbol, side, quantity, priceString, icebergQty, stopPrice, recvWindow):
    if not IsAPIKeySecretSet():
        raise Exception('API Key or Secret is not set. Set that before making this call.')

    timeStamp = GetTimeStamp()

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


def API_Post_BuyMarketOrder(symbol, quantity, icebergQty=None, stopPrice=None, recvWindow=5000):
    return API_Post_MarketOrder(symbol, "buy", quantity, icebergQty, stopPrice, recvWindow)

def API_Post_SellMarketOrder(symbol, quantity, icebergQty=None, stopPrice=None, recvWindow=5000):
    return API_Post_MarketOrder(symbol, "sell", quantity, icebergQty, stopPrice, recvWindow)

def API_Post_MarketOrder(symbol, side, quantity, icebergQty, stopPrice, recvWindow):
    if not IsAPIKeySecretSet():
        raise Exception('API Key or Secret is not set. Set that before making this call.')

    timeStamp = GetTimeStamp()

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


def API_Get_OrderStatus(symbol, orderId, recvWindow=5000):
    if not IsAPIKeySecretSet():
        raise Exception('API Key or Secret is not set. Set that before making this call.')

    timeStamp = GetTimeStamp()
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


def API_Delete_Order(symbol, orderId, recvWindow=5000):
    if not IsAPIKeySecretSet():
        raise Exception('API Key or Secret is not set. Set that before making this call.')

    timeStamp = GetTimeStamp()
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


def API_Get_OpenBuyOrders(symbol, recvWindow=5000):
    ordersJData = API_Get_OpenOrders(symbol, recvWindow)

    returnList = []
    for order in ordersJData:
        if order['side'].lower() == "buy":
            returnList.append(order)

    return returnList

def API_Get_OpenSellOrders(symbol, recvWindow=5000):
    ordersJData = API_Get_OpenOrders(symbol, recvWindow)

    returnList = []
    for order in ordersJData:
        if order['side'].lower() == "sell":
            returnList.append(order)

    return returnList

def API_Get_OpenOrders(symbol, recvWindow=5000):
    if not IsAPIKeySecretSet():
        raise Exception('API Key or Secret is not set. Set that before making this call.')

    timeStamp = GetTimeStamp()
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


def API_Get_Balance(currency):
    accountJData = API_Get_AccountInfo()

    for balance in accountJData['balances']:
        if currency.lower() == balance['asset'].lower():
            return balance


def API_Get_AccountInfo(recvWindow=5000):
    if not IsAPIKeySecretSet():
        raise Exception('API Key or Secret is not set. Set that before making this call.')

    timeStamp = GetTimeStamp()
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


# Waiting for this API to be finished.  Do not use yet
# def API_Post_Withdraw(asset, address, amount, recvWindow=5000):
#     if not IsAPIKeySecretSet():
#         raise Exception('API Key or Secret is not set. Set that before making this call.')
#
#     timeStamp = GetTimeStamp()
#     totalParams = "asset=" + asset.upper() + "&address=" + address + "&amount=" + str(amount) + "&recvWindow=" + str(recvWindow) + "&timestamp=" + timeStamp
#
#     PrintAndLog("totalParams = " + totalParams)
#     signature = GetBinanceSignature(totalParams)
#     PrintAndLog("signature = " + signature)
#
#     url = "https://www.binance.com/wapi/v1/withdraw.html?" + totalParams + "&signature=" + signature
#     PrintAndLog("url = " + url)
#
#     response = requests.post(url, headers=GetBinanceHeader(), timeout=RequestTimeout_seconds)
#     if (response.ok):
#         responseData = response.content
#         jData = json.loads(responseData)
#
#         PrintAndLog("API_Post_Withdraw jData = " + str(jData))
#         return jData
#
#     else:
#         # If response code is not ok (200), print the resulting http error code with description
#         PrintAndLog("response = " + str(response.content))
#         response.raise_for_status()
