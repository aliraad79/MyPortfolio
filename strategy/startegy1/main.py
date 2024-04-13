from MyData.read import read, Instrument
from analysis.indicator import SmallDataFilter, SMAFilter, IchimokuFilter, ADXFilter
import pandas as pd
from util.cli_utils import print_csv_dict_stock_name

def get_indicator_filtered_stocks(stocks: dict[str, pd.DataFrame]):
    # Start chain of filters
    start_of_chain = SmallDataFilter()
    # Add chain
    start_of_chain.set_next(SMAFilter()).set_next(IchimokuFilter()).set_next(
        ADXFilter()
    )
    return start_of_chain.filter(stocks)


def main():
    all_stock = read(Instrument.STOCK_ALL)
    indicator_filtered_stocks = get_indicator_filtered_stocks(all_stock)
    print_csv_dict_stock_name(indicator_filtered_stocks)
