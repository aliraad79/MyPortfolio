import pandas as pd
import os
from . import IRAN_STOCK_DATA_PATH, CRYPTO_DATA_PATH, OIL_DATA_PATH, MATALS_DATA_PATH
from .instrument import Instrument


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
        if stock_name != ".keep"
    }


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

def read_silver_monthly(_from="2020") -> pd.DataFrame:
    df = pd.read_csv(f"{MATALS_DATA_PATH}/silver_monthly.csv")

    return _convert_yfianace_data_to_standard_format(df)[_from:]


def read(instrument: Instrument, *args):
    match instrument:
        case Instrument.STOCK_ALL:
            return read_all_iran_stocks()
        case Instrument.STOCK:
            return read_iran_stock_as_pandas(args[0])
        case Instrument.STOCK_INDEX:
            return read_iran_main_stock_index()
        case Instrument.CRYPTO:
            return read_crypto_data(args[0])
        case Instrument.OIL:
            return read_brent_crude_oil_daily()
        case Instrument.SILVER:
            return read_silver_monthly()
