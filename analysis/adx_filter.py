from analysis.indicator import add_adx
from analysis.indicator_filter import IndicatorFilter

import pandas as pd


class ADXFilter(IndicatorFilter):
    def run_filter(self, stock_name: str, stock_df: pd.DataFrame):
        add_adx(stock_df)
        if stock_df["ADX_14"][-1] > 25:
            if self.verbose:
                print(f"Good movement has found in {stock_name}")
            return (stock_name, stock_df)
        raise Exception()
