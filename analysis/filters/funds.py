from pytse_client import Ticker
import pandas as pd


def filter_not_Funds(stocks_dict: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
    return {
        stock_name: df
        for stock_name, df in stocks_dict.items()
        if Ticker(stock_name.replace(".csv", "")).nav == None
    }
