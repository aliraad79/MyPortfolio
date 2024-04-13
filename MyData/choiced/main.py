import pandas as pd
import pandas_ta as ta


stocks = [
    ("khodro", "خودرو"),
    ("Family", "فملی"),
    ("Shasta", "شستا"),
    ("Folad", "فولاد"),
    ("Saderat", "وبصادر"),
    ("KARA-ETF", "کارا"),
]

cryptos = [
    ("btc", "BTC-USD"),
    ("eth", "ETH-USD"),
    ("doge", "DOGE-USD"),
    ("trx", "TRX-USD"),
    ("bnb", "BNB-USD"),
    ("shiba", "SHIB-USD"),
    ("sand", "SAND-USD"),
]

# Crypto
for _,crypto in cryptos:
    crypto_ohlc = pd.read_csv(f"{crypto}.csv")
    if "Date" in crypto_ohlc.columns:
        crypto_ohlc.columns = ["date", "open", "high", "low", "close", "adjClose", "volume"]
        crypto_ohlc.set_index(pd.DatetimeIndex(crypto_ohlc["date"]), inplace=True)
        crypto_ohlc = crypto_ohlc[["open", "high", "low", "close", "volume"]]
        crypto_ohlc.to_csv(f"./{crypto}.csv")


# Prepare Data
dfs = []
all_things = stocks + cryptos
for name, stock in all_things:
    df = pd.read_csv(f"{stock}.csv")
    df.set_index(pd.DatetimeIndex(df["date"]), inplace=True)
    df = df[["open", "close", "high", "low", "volume"]]
    df["tic"] = name
    df = df.ffill()
    df.ta.ichimoku(append=True)
    # df.ta.rsi(append=True)
    # df.ta.cci(append=True)
    dfs.append(df)

final = pd.concat(dfs, join="inner")
final = final[final.groupby("date").count()["tic"] == len(dfs)]
final["date"] = final.index
final = final.reset_index(drop=True)
final = final.sort_values("date")
final = final.reset_index(drop=True)
final.to_csv("final.csv")
