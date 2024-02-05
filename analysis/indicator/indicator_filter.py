from abc import ABC, abstractmethod
import pandas as pd


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: "Handler") -> "Handler":
        pass

    @abstractmethod
    def filter(self, stocks: dict[str, pd.DataFrame]):
        pass


class IndicatorFilter(ABC):
    def __init__(self, verbose=False) -> None:
        super().__init__()
        self.verbose = verbose
        self._next_handler: Handler = None

    def filter(self, stocks: dict[str, pd.DataFrame]):
        target_stocks = {}
        for stock_name, df in stocks.items():
            try:
                target_stock = self.run_filter(stock_name, df)
                target_stocks[target_stock[0]] = target_stock[1]
            except:
                if self.verbose:
                    print(f"{stock_name} has raise exception. len={len(df)}")

        if self._next_handler:
            return self._next_handler.filter(target_stocks)
        return target_stocks

    @abstractmethod
    def run_filter(self, stock_name: str, df: pd.DataFrame) -> tuple[str, pd.DataFrame]:
        ...

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler
