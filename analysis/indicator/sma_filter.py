from .indicators import add_smas
from .indicator_filter import IndicatorFilter

import pandas as pd


class SMAFilter(IndicatorFilter):
    def __init__(self, verbose=False, lines=[5, 10, 20, 50]) -> None:
        super().__init__(verbose)
        self.lines = lines

    def run_filter(self, stock_name: str, stock_df: pd.DataFrame):
        add_smas(stock_df)
        close_price = stock_df["close"].iloc[-1]
        flag = True
        for line in self.lines:
            if stock_df[f"SMA_{line}"].iloc[-1] > close_price:
                flag = False
            if self.verbose:
                print(f"Bullish stock is found {stock_name}")

        if flag:
            return (stock_name, stock_df)
