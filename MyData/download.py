from pytse_client import download, download_financial_indexes
import pandas_datareader.data as pdr
import yfinance as yfin
import pandas as pd


IRAN_STOCK_DATA_PATH = "MyData/ISM"
CRYPTO_DATA_PATH = "MyData/crypto"


def download_and_save_all_iran_sotck_data():
    download("all", write_to_csv=True, base_path=IRAN_STOCK_DATA_PATH)


def download_and_save_iran_sotck(stock_name):
    download(stock_name, write_to_csv=True, base_path=IRAN_STOCK_DATA_PATH)


def download_and_save__iran_stock_index():
    download_financial_indexes(
        symbols="شاخص کل", write_to_csv=True, base_path=IRAN_STOCK_DATA_PATH
    )


def download_crypto_daily(coin_symbol:str) -> pd.DataFrame:
    yfin.pdr_override()

    return pdr.get_data_yahoo(coin_symbol, start="2020-01-01", end="2023-12-01")


def download_and_save_crypto_daily(coin_symbol:str):
    data = download_crypto_daily(coin_symbol)
    data.to_csv(f"{CRYPTO_DATA_PATH}/BTCUSD.csv")
    return data
