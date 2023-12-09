from pytse_client import download


def download_and_save_all_data():
    download("all", write_to_csv=True, base_path="MyData/ISM")

def download_and_save(stock_name):
    download(stock_name, write_to_csv=True, base_path="MyData/ISM")
