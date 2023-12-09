import pandas as pd

BASE_DATA_PATH = "MyData/ISM"


def read_stock_as_pandas(stock_name) -> pd.DataFrame:
    df = pd.read_csv(f"{BASE_DATA_PATH}/{stock_name}.csv")
    df.set_index(pd.DatetimeIndex(df["date"]), inplace=True)
    df = df[["close", "open", "high", "low", "volume"]]
    return df
