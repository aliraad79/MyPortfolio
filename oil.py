from MyData import download,read

download.download_and_save_brent_crude_oil_daily()
df = read.read_brent_crude_oil_daily()
print(df)
