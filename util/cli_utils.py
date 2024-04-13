import arabic_reshaper
from bidi.algorithm import get_display


def convert(text):
    reshaped_text = arabic_reshaper.reshape(text)
    converted = get_display(reshaped_text)
    return converted


def print_csv_dict_stock_name(stock_names: dict):
    print([convert(i.split(".csv")[0]) for i in stock_names.keys()])

def print_csv_list_stock_name(stock_names: list):
    print([convert(i.split(".csv")[0]) for i in stock_names])