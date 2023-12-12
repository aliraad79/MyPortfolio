from .indicators import add_smas
from .indicator_filter import IndicatorFilter

import pandas as pd


class SMAFilter(IndicatorFilter):
    def run_filter(self, stock_name: str, stock_df: pd.DataFrame):
        add_smas(stock_df)
        close_price = stock_df["close"].iloc[-1]
        if (
            stock_df["SMA_5"].iloc[-1] < close_price
            and stock_df["SMA_10"].iloc[-1] < close_price
            and stock_df["SMA_20"].iloc[-1] < close_price
            and stock_df["SMA_50"].iloc[-1] < close_price
        ):
            if self.verbose:
                print(f"Bullish stock is found {stock_name}")
            return (stock_name, stock_df)
