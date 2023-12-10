import numpy as np
import matplotlib.pyplot as plt


def plot_df_with_pattern(df, start_point, end_point):
    fig, ax = plt.subplots(figsize=(16, 4))
    ax.plot(df.index, df['close'])
    
    # adjust labels
    ax.set_ylabel("Close Price")
    
    # assign title
    ax.set_title("Stock Price", size=15)
    
    # highlight a time range
    ax.axvspan(start_point, end_point, color="blue", alpha=0.3)
    plt.show()
