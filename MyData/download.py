from pytse_client import download, download_financial_indexes
import pandas_datareader.data as pdr
import yfinance as yfin
import pandas as pd
from .instrument import Instrument

from . import IRAN_STOCK_DATA_PATH, CRYPTO_DATA_PATH, OIL_DATA_PATH


def download_and_save_all_iran_sotck_data():
    download("all", write_to_csv=True, base_path=IRAN_STOCK_DATA_PATH)


def download_and_save_iran_sotck(stock_name):
    download(stock_name, write_to_csv=True, base_path=IRAN_STOCK_DATA_PATH)


def download_and_save_iran_stock_index():
    download_financial_indexes(
        symbols="شاخص کل", write_to_csv=True, base_path=IRAN_STOCK_DATA_PATH
    )


def download_crypto_daily(coin_symbol: str) -> pd.DataFrame:
    yfin.pdr_override()

    return pdr.get_data_yahoo(coin_symbol, start="2020-01-01", end="2023-12-01")


def download_and_save_crypto_daily(coin_symbol: str):
    data = download_crypto_daily(coin_symbol)
    data.to_csv(f"{CRYPTO_DATA_PATH}/{coin_symbol}.csv")
    return data


def download_brent_crude_oil_daily() -> pd.DataFrame:
    yfin.pdr_override()

    return pdr.get_data_yahoo("BZ=F", start="2020-01-01", end="2023-12-01")


def download_and_save_brent_crude_oil_daily():
    data = download_brent_crude_oil_daily()
    data.to_csv(f"{OIL_DATA_PATH}/BR.csv")
    return data

def download_silver_monthly() -> pd.DataFrame:
    yfin.pdr_override()

    return pdr.get_data_yahoo("BZ=F", start="2020-01-01", end="2023-12-01")


def download_and_save_silver_monthly():
    data = download_silver_monthly()
    data.to_csv(f"{MATALS_DATA_PATH}/silver_monthly.csv")
    return data


def update_all_datas():
    download_and_save_all_iran_sotck_data()
    download_and_save_iran_stock_index()
    download_and_save_crypto_daily()
    download_and_save_brent_crude_oil_daily()
    download_and_save_silver_monthly()


def download(instrument: Instrument, *args):
    match instrument:
        case Instrument.ALL:
            return update_all_datas()
        case Instrument.STOCK_ALL:
            return download_and_save_all_iran_sotck_data()
        case Instrument.STOCK:
            return download_and_save_iran_sotck(args[0])
        case Instrument.STOCK_INDEX:
            return download_and_save_iran_stock_index()
        case Instrument.CRYPTO:
            return download_and_save_crypto_daily(args[0])
        case Instrument.OIL:
            return download_and_save_brent_crude_oil_daily()
        case Instrument.SILVER:
            return download_and_save_silver_monthly()
