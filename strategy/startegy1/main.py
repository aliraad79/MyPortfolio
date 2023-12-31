from MyData import read
from analysis.indicator import SmallDataFilter, SMAFilter, IchimokuFilter, ADXFilter
import pandas as pd


def get_indicator_filtered_stocks(stocks: dict[str, pd.DataFrame]):
    # Start chain of filters
    start_of_chain = SmallDataFilter()
    # Add chain
    start_of_chain.set_next(SMAFilter()).set_next(IchimokuFilter()).set_next(
        ADXFilter()
    )
    return start_of_chain.filter(stocks)


def main():
    all_stock = read.read_all_iran_stocks()
    indicator_filtered_stocks = get_indicator_filtered_stocks(all_stock)
    print(indicator_filtered_stocks.keys())
