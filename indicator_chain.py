from MyData.read import read, Instrument
from analysis.indicator import SmallDataFilter, SMAFilter, IchimokuFilter, ADXFilter

# download.download_and_save_all_iran_sotck_data()

all_stock = read(Instrument.ALL)

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
