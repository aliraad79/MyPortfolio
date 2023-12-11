from MyData import read
from analysis.indicator import SmallDataFilter, SMAFilter, IchimokuFilter, ADXFilter


def get_indicator_filtered_stocks():
    all_stock = read.read_all_stocks()

    # Start chain of filters
    start_of_chain = SmallDataFilter()
    # Add chain
    start_of_chain.set_next(SMAFilter()).set_next(IchimokuFilter()).set_next(ADXFilter())
    return start_of_chain.filter(all_stock)

def main():
    indicator_filtered_stocks = get_indicator_filtered_stocks()
    print(indicator_filtered_stocks.keys())

