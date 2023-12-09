from MyData import download, read
from analysis import indicator

# download.download_and_save_all_data()

df = read.read_stock_as_pandas("وتجارت")

indicator.add_my_indicators(df)
print(df)
