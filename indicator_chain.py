from MyData import download, read
from analysis.indicator import SmallDataFilter, SMAFilter, IchimokuFilter, ADXFilter

# download.download_and_save_all_data()

df = read.read_stock_as_pandas("وتجارت")["2020":]

# indicator.add_my_indicators(df)
all_stock = read.read_all_stocks()

# Start chain of filters
small_data_fil = SmallDataFilter()
small_data_filtred = small_data_fil.filter(all_stock)

sma_fil = SMAFilter()
sma_filterd = sma_fil.filter(small_data_filtred)

ichi_fil = IchimokuFilter()
ichi_filtered = ichi_fil.filter(sma_filterd)

adx_fil = ADXFilter()
adx_filtered = adx_fil.filter(ichi_filtered)


print(adx_filtered.keys())
