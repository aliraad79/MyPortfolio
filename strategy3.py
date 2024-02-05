from analysis.indicator import SMAFilter, IchimokuFilter, ADXFilter
from MyData import read, Instrument, download
from util.cli_utils import print_csv_list_stock_name


# download(Instrument.STOCK_ALL_INDICIES)
all_indices = read(Instrument.STOCK_ALL_INDICIES)

sma_fil = SMAFilter(verbose=True)
sma_filterd = sma_fil.filter(all_indices)

print_csv_list_stock_name(sma_filterd)

ichi_fil = IchimokuFilter(verbose=True)
ichi_filtered = ichi_fil.filter(sma_filterd)

print_csv_list_stock_name(ichi_filtered)

adx_fil = ADXFilter(verbose=True)
adx_filtered = adx_fil.filter(ichi_filtered)


print_csv_list_stock_name(adx_filtered)