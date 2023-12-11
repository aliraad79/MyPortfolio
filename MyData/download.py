from pytse_client import download, download_financial_indexes
import pandas_datareader.data as pdr
import yfinance as yfin
import pandas as pd


DATA_PATH = "MyData/ISM"


def download_and_save_all_data():
    download("all", write_to_csv=True, base_path=DATA_PATH)


def download_and_save(stock_name):
    download(stock_name, write_to_csv=True, base_path=DATA_PATH)


def download_and_save_stock_index():
    download_financial_indexes(
        symbols="شاخص کل", write_to_csv=True, base_path=DATA_PATH
    )


def download_coin_daily() -> pd.DataFrame:
    yfin.pdr_override()

    return pdr.get_data_yahoo("BTC-USD", start="2020-01-01", end="2023-12-01")


def download_and_save_coin_daily():
    data = download_coin_daily()
    data.to_csv(f"{DATA_PATH}/BTCUSDT.csv")
    return data
