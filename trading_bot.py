import pandas as pd
import requests
from selenium.common.exceptions import TimeoutException
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import json
import requests

def getData(ticker):

    file = open("alphavantage.json", "r")
    api_key = json.loads(file.read())["alpha_vantage_key"]
    end_point = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=%s&market=USD&outputsize=full&apikey=%s"%(ticker, api_key)
    r = requests.get(end_point)

    if r.status_code == 200:

        print("API Success")

        assert "Information" not in json.loads(r.content).keys()


        print("Auth Success")
        my_json = json.loads(r.content)
        print(my_json["Meta Data"])
        col_dict={"index":"datetime"}
        data = pd.DataFrame(my_json['Time Series (Digital Currency Daily)']).T.reset_index().rename(columns=col_dict)
        data["datetime"]=pd.to_datetime(data["datetime"])
        final_df = data.sort_values("datetime").reset_index(drop=True)
        return final_df

    
