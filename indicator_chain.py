from MyData.read import read, Instrument
from MyData.download import download
from util.cli_utils import print_csv_list_stock_name
from analysis.indicator import SmallDataFilter, SMAFilter, IchimokuFilter, ADXFilter

# download(Instrument.STOCK_ALL)

all_stock = read(Instrument.STOCK_ALL)

# Start chain of filters
small_data_fil = SmallDataFilter()
small_data_filtred = small_data_fil.filter(all_stock)

sma_fil = SMAFilter()
sma_filterd = sma_fil.filter(small_data_filtred)

ichi_fil = IchimokuFilter()
ichi_filtered = ichi_fil.filter(sma_filterd)

adx_fil = ADXFilter()
adx_filtered = adx_fil.filter(ichi_filtered)


print_csv_list_stock_name(adx_filtered.keys())
