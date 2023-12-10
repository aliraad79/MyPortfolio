from analysis.indicator import add_smas
import pandas as pd
from indicator_filter import IndicatorFilter


class IchimokuFilter(IndicatorFilter):
    def run_filter(self, stock_name: str, stock_df: pd.DataFrame):
        add_smas(stock_df)
        if (
            stock_df["SMA_5"][-1] < stock_df["close"][-1]
            and stock_df["SMA_10"][-1] < stock_df["close"][-1]
            and stock_df["SMA_20"][-1] < stock_df["close"][-1]
            and stock_df["SMA_50"][-1] < stock_df["close"][-1]
        ):
            if self.verbose:
                print(f"Bullish stock is found {stock_name}")
            return (stock_name, stock_df)
