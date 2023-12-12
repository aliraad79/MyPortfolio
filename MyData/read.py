import pandas as pd
import os

BASE_DATA_PATH = "MyData/ISM"


def read_iran_stock_as_pandas(stock_name, _from="2020") -> pd.DataFrame:
    df = pd.read_csv(f"{BASE_DATA_PATH}/{stock_name}.csv")
    df.set_index(pd.DatetimeIndex(df["date"]), inplace=True)
    df = df[["close", "open", "high", "low", "volume"]]
    return df[_from:]


def read_all_iran_stocks() -> list[pd.DataFrame]:
    all_stocks = [i.replace(".csv", "") for i in os.listdir(BASE_DATA_PATH)]
    return {
        stock_name: read_iran_stock_as_pandas(stock_name) for stock_name in all_stocks
    }


def read_iran_main_stock_index(_from="2020") -> pd.DataFrame:
    df = pd.read_csv(f"{BASE_DATA_PATH}/شاخص كل.csv")
    df.set_index(pd.DatetimeIndex(df["date"]), inplace=True)
    df = df[["close", "open", "high", "low", "volume"]]
    return df[_from:]


def read_crypto_data(coin: str = "BTCUSDT", _from="2020") -> pd.DataFrame:
    df = pd.read_csv(f"{BASE_DATA_PATH}/{coin}.csv")
    df["date"] = df["Date"]
    df.set_index(pd.DatetimeIndex(df["date"]), inplace=True)
    df = df[["Close", "Open", "High", "Low", "Volume"]]
    df.columns = ["close", "open", "high", "low", "volume"]
    return df[_from:]
