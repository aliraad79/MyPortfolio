from MyData.read import read, Instrument
from analysis.indicator import SmallDataFilter, SMAFilter, IchimokuFilter, ADXFilter
import pandas as pd
import arabic_reshaper
from bidi.algorithm import get_display


def convert(text):
    reshaped_text = arabic_reshaper.reshape(text)
    converted = get_display(reshaped_text)
    return converted


def get_indicator_filtered_stocks(stocks: dict[str, pd.DataFrame]):
    # Start chain of filters
    start_of_chain = SmallDataFilter()
    # Add chain
    start_of_chain.set_next(SMAFilter()).set_next(IchimokuFilter()).set_next(
        ADXFilter()
    )
    return start_of_chain.filter(stocks)


def main():
    all_stock = read(Instrument.ALL)
    indicator_filtered_stocks = get_indicator_filtered_stocks(all_stock)
    print([convert(i.split(".csv")[0]) for i in indicator_filtered_stocks.keys()])
