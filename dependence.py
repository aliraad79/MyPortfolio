from analysis.dependence.regression import regress
from MyData import read
import pandas as pd
import numpy as np

stock = read.read_stock_as_pandas("وتجارت")["close"]

rf_df = pd.Series(data=np.repeat(0.0216, len(stock)), index=stock.index)

stock_excess_return = pd.DataFrame(data=stock.pct_change() - rf_df, index=stock.index, columns=["stock_excess"]).dropna()

main_index = read.read_main_stock_index()["close"].pct_change().dropna()
main_index_excess = pd.DataFrame(
    data=main_index - rf_df, index=stock.index, columns=["market_excess"]
).dropna()

exp_var = main_index_excess.copy()

result = regress(stock_excess_return, exp_var)
print(result.summary())
