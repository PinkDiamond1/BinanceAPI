#!/usr/bin/env python

__author__ = "Joey Zacherl"
__credits__ = ["Joey Zacherl", "https://pypi.python.org/pypi/websocket-client"]
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
import websocket
import thread
import time
import ssl

# Websocket example was referenced from: https://pypi.python.org/pypi/websocket-client
# Install using command: pip install websocket-client

def on_message(ws, message):
    PrintAndLog(str(message))

def on_error(ws, error):
    PrintAndLog(str(error))

def on_close(ws):
    PrintAndLog("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(60):
            time.sleep(1)
            # ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        PrintAndLog("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)

    # Choose which URL you'd like to subscribe to
    # url = "wss://stream.binance.com:9443/ws/ethbtc@depth"
    # url = "wss://stream.binance.com:9443/ws/ethbtc@kline_1m"
    # url = "wss://stream.binance.com:9443/ws/ethbtc@aggTrade"
    url = "wss://stream.binance.com:9443/ws/ethbtc@depth"
    ws = websocket.WebSocketApp(url, on_message = on_message, on_error = on_error, on_close = on_close)
    ws.on_open = on_open
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
