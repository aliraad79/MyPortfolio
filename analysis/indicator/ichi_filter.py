from .indicator import add_ichimoku_cloud
from .indicator_filter import IndicatorFilter

import pandas as pd


class IchimokuFilter(IndicatorFilter):
    def run_filter(self, stock_name: str, stock_df: pd.DataFrame):
        add_ichimoku_cloud(stock_df)
        if (
            stock_df["ISA_9"].iloc[-1] < stock_df["close"].iloc[-1]
            and stock_df["ISB_26"].iloc[-1] < stock_df["close"].iloc[-1]
        ):
            if self.verbose:
                print(f"Upper than cload stock is found {stock_name}")
            return (stock_name, stock_df)
