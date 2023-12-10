from abc import ABC, abstractmethod
import pandas as pd


class IndicatorFilter(ABC):
    def __init__(self, verbose=False) -> None:
        super().__init__()
        self.verbose = verbose

    def filter(self, stocks: dict[str, pd.DataFrame]):
        target_stocks = {}
        for stock_name, df in stocks.items():
            try:
                target_stock = self.run_filter(stock_name, df)
                target_stocks[target_stock[0]] = target_stock[1]
            except:
                if self.verbose:
                    print(f"{stock_name} has raise exception. len={len(stock_name)}")
        return target_stocks

    @abstractmethod
    def run_filter(self, stock_name: str, df: pd.DataFrame) -> tuple[str, pd.DataFrame]:
        ...
