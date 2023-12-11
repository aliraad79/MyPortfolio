import requests
from bs4 import BeautifulSoup
from datetime import date


class DataRow:
    def __init__(self, forecast, symbol, actual, time) -> None:
        self.forecast = forecast
        self.symbol = symbol
        self.actual = actual
        self.time = time

    def __repr__(self) -> str:
        return f"<{self.symbol}, {self.time}, {self.forecast}, {self.actual}>"

    def to_csv(self) -> str:
        return f"{self.symbol},{self.time},{self.actual},{self.forecast}"


def write_to_csv(datas):
    current_date = date.today()
    with open(f"../MyData/forexFactory/{current_date}.csv", "w+") as file:
        file.write(",Symbol,Time,Actual,ForeCast\n")
        for idx, data_row in enumerate(datas):
            file.write(f"{idx},{data_row.to_csv()}\n")


BASE_URL = "https://www.forexfactory.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-GB,en;q=0.5",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-GPC": "1",
}

response = requests.get(f"{BASE_URL}/#upnext", headers=headers)

soap = BeautifulSoup(response.text, features="lxml")
table = soap.find(attrs={"class": "calendar__table"})


datas = []
for row in table.find_all("tr")[4:]:
    symbol = row.find("td", attrs={"class": "calendar__cell calendar__currency"}).text
    actual = row.find("td", attrs={"class": "calendar__cell calendar__actual"}).text
    forecast = row.find("td", attrs={"class": "calendar__cell calendar__forecast"}).text
    time = row.find("td", attrs={"class": "calendar__cell calendar__time"}).text
    datas.append(DataRow(forecast, symbol, actual, time))

write_to_csv(datas)
