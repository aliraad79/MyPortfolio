from MyData import read
from analysis.pattern.pattern import find_patterns
from chart.pattern import plot_df_with_pattern
import pandas as pd
import numpy as np


df = read.read_stock_as_pandas("وتجارت")["2021":]

prices = pd.Series(data=df["close"].values)
prices.index = np.linspace(1, len(prices), len(prices))

dates = pd.Series(data=df.index.values)
dates.index = np.linspace(1, len(df.index), len(df.index))

patterns = find_patterns(prices)

for name, lis in patterns.items():
    print(f"For pattern {name}")
    
    pattern_points = [(dates.iloc[int(j[0])], dates.iloc[int(j[1])]) for j in lis]
    
    plot_df_with_pattern(df, pattern_points)


