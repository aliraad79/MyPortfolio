from analysis.indicator import add_smas
from analysis.indicator_filter import IndicatorFilter

import pandas as pd


class SmallDataFilter(IndicatorFilter):
    def run_filter(self, stock_name: str, stock_df: pd.DataFrame):
        if len(stock_df) < 20:
            if self.verbose:
                print(f"stock has small amount of data {stock_name}")
            raise Exception()
        else:
            return (stock_name, stock_df)
