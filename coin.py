from MyData.download import download, Instrument
from MyData.read import read, Instrument


download(Instrument.CRYPTO, "BTC-USD")

data = read(Instrument.CRYPTO, "BTC-USD")

print(data)
