from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from MyData.read import read_all_iran_stocks
from MyData.download import download_and_save_all_iran_sotck_data

from analysis.indicator import SmallDataFilter
from chart.randomForest import plot_df
import pandas as pd
from tqdm import tqdm

N = 0.80


def main(download_data=False):
    if download_data:
        download_and_save_all_iran_sotck_data()
    dfs = read_all_iran_stocks()

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

    plot_df(scores, N * 100)
