#!/usr/bin/env python

__author__ = "Joey Zacherl"
__license__ = "MIT"
__version__ = "1.0.0"
__description__ = "Binance API integration"
__email__ = "Joey.Zacherl@gmail.com"

import logging
from datetime import datetime
import pytz

def InitLogging():
    logging.basicConfig(level=logging.DEBUG, filename="logfile", filemode="a+", format="%(asctime)-15s %(levelname)-8s %(message)s")
    logging.Formatter.converter = GetCustomTime

    # requests spams the logging module with stuff I don't need, so don't show them unless it's a warning
    logging.getLogger("requests").setLevel(logging.ERROR)

def GetCustomTime(*args):
    utc_dt = pytz.utc.localize(datetime.utcnow())
    my_tz = pytz.timezone("US/Pacific")
    converted = utc_dt.astimezone(my_tz)
    return converted.timetuple()

def PrintAndLog(message):
    print message
    logging.info(message)

def PrintAndLogError(message):
    print message
    logging.error(message)