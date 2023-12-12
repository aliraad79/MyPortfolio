import matplotlib.pyplot as plt
import pandas as pd


def plot_df(serie: pd.DataFrame, line):
    plt.scatter(serie.name, serie.score) 

    # adjust labels
    plt.ylabel("RF scores")

    # assign title
    plt.title("Rf scores for all of iran stock market", size=15)

    plt.axhline(line)

    plt.show()
