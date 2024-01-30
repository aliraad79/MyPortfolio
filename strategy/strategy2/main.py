from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from MyData.read import read, Instrument
from MyData.download import download, Instrument

from analysis.indicator import SmallDataFilter
from analysis.filters.funds import filter_not_Funds
from chart.randomForest import plot_df
import pandas as pd
from tqdm import tqdm
from strategy.startegy1.main import get_indicator_filtered_stocks

N = 70  # in precent


def run(download_data=False, plot_data=False):
    if download_data:
        download(Instrument.STOCK_ALL)

    dfs = read(Instrument.STOCK_ALL)[:50]

    scores = filter_with_rf(dfs, plot_data)
    scores_dict = {
        i["name"]: read(Instrument.STOCK, i["name"]) for i in scores.to_dict("records")
    }

    datas = get_indicator_filtered_stocks(scores_dict)

    datas = filter_not_Funds(datas)
    print(datas)


def filter_with_rf(dfs, plot_data):
    small_data_fil = SmallDataFilter()
    small_data_filtred = small_data_fil.filter(dfs)

    scores = []
    for stock_name, df in tqdm(small_data_filtred.items()):
        y = df["close"] > df["close"].shift()

        X_train, X_test, y_train, y_test = train_test_split(df, y)

        clf = RandomForestClassifier(max_depth=10, random_state=0)
        clf.fit(X_train, y_train)
        score = clf.score(X_test, y_test)

        score = round(score * 100, 3)
        scores.append([stock_name, score])

    scores.sort(key=lambda x: x[1])
    scores = pd.DataFrame(scores, columns=["name", "score"])

    print("Mean of scores: ", scores.score.mean())
    print("Std of scores: ", scores.score.std())

    if plot_data:
        plot_df(scores, N)
    return scores[scores.score > N]
