from MyData.read import read, Instrument
from MyData.download import download, Instrument

download(Instrument.OIL)
df = read(Instrument.OIL)
print(df)
