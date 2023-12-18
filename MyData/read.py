import pandas as pd
import os
from . import IRAN_STOCK_DATA_PATH, CRYPTO_DATA_PATH, OIL_DATA_PATH


def read_iran_stock_as_pandas(stock_name_csv_file, _from="2020") -> pd.DataFrame:
    df = pd.read_csv(f"{IRAN_STOCK_DATA_PATH}/{stock_name_csv_file}")
    df.set_index(pd.to_datetime(df["date"]), inplace=True)
    df = df[["close", "open", "high", "low", "volume"]]
    df = df[~df.index.duplicated(keep="first")]
    return df[_from:]


def read_all_iran_stocks() -> dict[pd.DataFrame]:
    return {
        stock_name: read_iran_stock_as_pandas(stock_name)
        for stock_name in os.listdir(IRAN_STOCK_DATA_PATH)
    }


def read_all_iran_stocks_close_as_pandas_sample() -> dict[pd.DataFrame]:
    return {
        stock_name.replace(".csv", ""): read_iran_stock_as_pandas(stock_name).close
        for stock_name in os.listdir(IRAN_STOCK_DATA_PATH)[:50]
    }


def read_sample_iran_stocks() -> dict[pd.DataFrame]:
    return {
        stock_name: read_iran_stock_as_pandas(stock_name)
        for stock_name in os.listdir(IRAN_STOCK_DATA_PATH)[:50]
    }


def read_list_of_stocks(stocks: list[str]) -> dict[pd.DataFrame]:
    return {stock_name: read_iran_stock_as_pandas(stock_name) for stock_name in stocks}


def read_iran_main_stock_index(_from="2020") -> pd.DataFrame:
    df = pd.read_csv(f"{IRAN_STOCK_DATA_PATH}/شاخص كل.csv")
    df.set_index(pd.DatetimeIndex(df["date"]), inplace=True)
    df = df[["close", "open", "high", "low", "volume"]]
    return df[_from:]


def _convert_yfianace_data_to_standard_format(df):
    df["date"] = df["Date"]
    df.set_index(pd.DatetimeIndex(df["date"]), inplace=True)
    df = df[["Close", "Open", "High", "Low", "Volume"]]
    df.columns = ["close", "open", "high", "low", "volume"]
    return df


def read_crypto_data(coin: str = "BTCUSDT", _from="2020") -> pd.DataFrame:
    df = pd.read_csv(f"{CRYPTO_DATA_PATH}/{coin}.csv")

    return _convert_yfianace_data_to_standard_format(df)[_from:]


def read_brent_crude_oil_daily(_from="2020") -> pd.DataFrame:
    df = pd.read_csv(f"{OIL_DATA_PATH}/BR.csv")

    return _convert_yfianace_data_to_standard_format(df)[_from:]
