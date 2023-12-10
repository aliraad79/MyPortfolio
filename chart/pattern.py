import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.colors as mcolors


def plot_df_with_pattern(df, points):
    fig, ax = plt.subplots(figsize=(16, 4))
    ax.plot(df.index, df['close'])
    
    # adjust labels
    ax.set_ylabel("Close Price")
    
    # assign title
    ax.set_title("Stock Price", size=15)
    
    # highlight a time range
    for start_point, end_point in points:
        ax.axvspan(start_point, end_point, color=random.choice(list(mcolors.CSS4_COLORS.values())), alpha=0.3)
    plt.show()
