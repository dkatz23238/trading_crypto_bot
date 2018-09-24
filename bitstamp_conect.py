import pandas as pd
import requests
from selenium.common.exceptions import TimeoutException
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import json
import requests
import bitstamp.client

file = open("/Users/davidkatzaudio/Desktop/trading_bot/bitstamp.json", "r").read() #reads json formated string
stampUser = json.loads(file)["customer_id"]
stampKey = json.loads(file)["key"]
stampSecret = json.loads(file)["secret"]

trading_client = bitstamp.client.Trading(username=stampUser,key=stampKey,secret=stampSecret)

balance_response = ['btc_available',
                    'btc_balance',
                    'btc_reserved',
                    'fee',
                    'usd_available',
                    'usd_balance',
                    'usd_reserved']

assert list(trading_client.account_balance().keys()) == balance_response, "Response Incorrect. Please Check Credentials"

print("Success!")
