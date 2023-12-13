from sklearn.ensemble import RandomForestClassifier
from MyData.read import read_iran_stock_as_pandas

def train_rf_on_iran_stock(stock_name):
    df = read_iran_stock_as_pandas(stock_name)
    y = df["close"] > df["close"].shift()

    clf = RandomForestClassifier(max_depth=10, random_state=0)
    clf.fit(df, y)
    return clf
