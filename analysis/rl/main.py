from MyData.read import read_all_iran_stocks_close_as_pandas_sample
import pandas as pd
import numpy as np
from analysis.indicator.small_data_filter import SmallDataFilter

def pre_process_data(dfs):
    small_data_fil = SmallDataFilter()
    small_data_filtred = small_data_fil.filter(dfs)

    stocks_returns = pd.DataFrame(small_data_filtred).resample("1M").sum().to_period("M")
    stocks_returns = stocks_returns.pct_change()
    stocks_returns.fillna(0, inplace=True)
    stocks_returns.replace(np.inf, 0, inplace=True)
    return stocks_returns


def run():
    dfs = read_all_iran_stocks_close_as_pandas_sample()
    stocks_returns = pre_process_data(dfs)

    print(stocks_returns)
