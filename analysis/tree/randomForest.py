from sklearn.ensemble import RandomForestClassifier
from MyData.read import read, Instrument

def train_rf_on_iran_stock(stock_name):
    df = read(Instrument.STOCK_ALL,stock_name)
    y = df["close"] > df["close"].shift()

    clf = RandomForestClassifier(max_depth=10, random_state=0)
    clf.fit(df, y)
    return clf
