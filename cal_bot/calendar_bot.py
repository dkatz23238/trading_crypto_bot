from autom8 import *
import pandas as pd
import requests
from selenium.common.exceptions import TimeoutException
pd.options.display.max_columns = 999

def robust_get(my_bot, url):
    try:
        my_bot.driver.get(url)
    except TimeoutException as e:
        print(e)

def wipe(my_bot):

    my_bot.driver.quit()

def getNASDAQ():
    try:
        get = requests.get("http://www.advfn.com/nasdaq/nasdaq.asp")
        content = get.content
        df = pd.read_html(content)[-1]
        df.columns = df.iloc[1]
        df = df.drop(0).drop(1)
        return df
    except Exception as e:
        print(e)
        print("Trying Again...")
        sleep(2)
        getNasdaq()

def return_earnings_call(nasdaq_df):
    quarters_1 = ["1", "2", "3"]
    quarters_2 = ["1", "2", "3", "4"]

    my_strings = []

    for j in quarters:
        string_finder = "%s (%s) Q%s 2018 - Earnings Call Transcript" % (nasdaq_df.iloc[i, :]["Company Name"], nasdaq_df.iloc[i, :]["Symbol"], j)
        my_strings.append(string_finder)

    for j in quarters_2:
        string_finder = "%s (%s) Q%s 2017 - Earnings Call Transcript" % (nasdaq_df.iloc[i, :]["Company Name"], nasdaq_df.iloc[i, :]["Symbol"], j)
        my_strings.append(string_finder)
    return my_strings

#nasdaq_df = getNASDAQ()
nasdaq_df = pd.read_csv('unique_historic.csv').rename(columns={"0":"Symbol"})
company_list = pd.read_csv('companylist.csv')

print(list(nasdaq_df["Symbol"]))

df_calendars = {}

#all_dictionaries = []
#i=0
#gets_links_for_all_symbols
for i in range(len(nasdaq_df))[:]:
    url = "https://finance.yahoo.com/calendar/earnings?from=2018-08-19&to=2018-08-25&day=2018-08-20&symbol=%s"%nasdaq_df.Symbol.iloc[i]
    #%
    r = requests.get(url)
    p_source = r.content
    try:
        df = pd.read_html(p_source)[0]
        df_calendars[nasdaq_df.Symbol.iloc[i]] = df.to_json()
        print(df)
    except:
        print("No Data For %s"%nasdaq_df.Symbol.iloc[i])

try:
    os.mkdir("Outputs")
except:
    pass
for i in df_calendars.keys():
    pd.read_json(df_calendars[i]).to_csv("Outputs/%s.csv"%i)

#pd.DataFrame(json.loads(df_calendars[nasdaq_df.Symbol.iloc[i]]))
