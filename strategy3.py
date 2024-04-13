from analysis.indicator import SMAFilter, IchimokuFilter, ADXFilter
from MyData import read, Instrument, download
from util.cli_utils import print_csv_dict_stock_name


# download(Instrument.STOCK_ALL_INDICIES)
all_indices = read(Instrument.STOCK_ALL_INDICIES)

sma_fil = SMAFilter(lines=[10])
sma_filterd = sma_fil.filter(all_indices)

print_csv_dict_stock_name(sma_filterd)

ichi_fil = IchimokuFilter()
ichi_filtered = ichi_fil.filter(all_indices)

print_csv_dict_stock_name(ichi_filtered)

adx_fil = ADXFilter()
adx_filtered = adx_fil.filter(ichi_filtered)


print_csv_dict_stock_name(adx_filtered)