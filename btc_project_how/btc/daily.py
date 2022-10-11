from binance import Client
import pandas as pd
import awswrangler as wr
import os

api = os.environ.get("apikey")
secret = os.environ.get("secret")
coin = 'ETHBTC'

client = Client(api, secret)

tickers = client.get_all_tickers()

df = pd.DataFrame(tickers)

historical = client.get_historical_klines(coin, Client.KLINE_INTERVAL_1DAY, '1 Jan 2011')
historical

hist_df = pd.DataFrame(historical)
hist_df.columns = ['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 'Quote Asset Volume', 
                    'Number of Trades', 'TB Base Volume', 'TB Quote Volume', 'Ignore']
                    
#write_to_parquet_historical():
#    wr.s3.to_parquet(
#    df=hist_df,
#    path="s3://how-eng-dados-biss/btc/",
#    dataset=True)

wr.s3.to_parquet(
    df=df,
    path="s3://how-eng-dados-biss/btc/",
    dataset=True)

#hist_df['Open Time'] = pd.to_datetime(hist_df['Open Time']/1000, unit='s')
#hist_df['Close Time'] = pd.to_datetime(hist_df['Close Time']/1000, unit='s')

#numeric_columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Quote Asset Volume', 'TB Base Volume', 'TB Quote Volume']
#hist_df[numeric_columns] = hist_df[numeric_columns].apply(pd.to_numeric, axis=1)

