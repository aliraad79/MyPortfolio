from MyData.download import download_and_save_crypto_daily
from MyData.read import read_crypto_data


download_and_save_crypto_daily("BTC-USD")

data = read_crypto_data("BTCUSD")

print(data)
