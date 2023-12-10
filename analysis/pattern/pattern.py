from collections import defaultdict

import numpy as np
import pandas as pd
from scipy.signal import argrelextrema
from statsmodels.nonparametric.kernel_regression import KernelReg



def find_max_min(prices):
    model = KernelReg(prices.values, prices.index.values, var_type="c", bw="cv_ls")
    smooth_prices = pd.Series(
        data=model.fit([prices.index.values])[0], index=prices.index
    )  # index also from 1

    # use the minima and maxima from the smoothed timeseries
    # to identify true local minima and maxima in the original timeseres
    # by taking the maximum/minimum price within a t-1, t+1 window in the smoothed timeseries
    smooth_prices_max_indices = argrelextrema(smooth_prices.values, np.greater)[0]
    smooth_prices_min_indices = argrelextrema(smooth_prices.values, np.less)[0]

    price_max_indices = []
    for i in smooth_prices_max_indices:
        if 1 < i < len(prices) - 1:
            price_max_indices.append(prices.iloc[i - 2 : i + 2].idxmax())

    price_min_indices = []
    for i in smooth_prices_min_indices:
        if 1 < i < len(prices) - 1:
            price_min_indices.append(prices.iloc[i - 2 : i + 2].idxmin())

    price_max = prices.loc[price_max_indices]
    price_min = prices.loc[price_min_indices]
    max_min = pd.concat([price_max, price_min]).sort_index()
    max_min = max_min[
        ~max_min.duplicated()
    ]  # deduplicate points that are both maximum and minimum

    return max_min


def find_patterns(prices):
    max_min = find_max_min(prices)
    patterns = defaultdict(list)

    for i in range(5, len(max_min)):
        window = max_min.iloc[i - 5 : i]

        # pattern must play out in less than 36 days
        if window.index[-1] - window.index[0] > 35:
            continue

        # Using the notation from the paper to avoid mistakes
        e1, e2, e3, e4, e5 = window.iloc[:5]
        rtop_g1 = np.mean([e1, e3, e5])
        rtop_g2 = np.mean([e2, e4])

        # Head and Shoulders
        if (
            (e1 > e2)
            and (e3 > e1)
            and (e3 > e5)
            and (abs(e1 - e5) <= 0.03 * np.mean([e1, e5]))
            and (abs(e2 - e4) <= 0.03 * np.mean([e1, e5]))
        ):
            patterns["Head_and_Shoulders"].append((window.index[0], window.index[-1]))

        # Inverse Head and Shoulders
        elif (
            (e1 < e2)
            and (e3 < e1)
            and (e3 < e5)
            and (abs(e1 - e5) <= 0.03 * np.mean([e1, e5]))
            and (abs(e2 - e4) <= 0.03 * np.mean([e1, e5]))
        ):
            patterns["Inverse_Head_and_Shoulders"].append(
                (window.index[0], window.index[-1])
            )

        # Broadening Top
        elif (e1 > e2) and (e1 < e3) and (e3 < e5) and (e2 > e4):
            patterns["Broadening_Top"].append((window.index[0], window.index[-1]))

        # Broadening Bottom
        elif (e1 < e2) and (e1 > e3) and (e3 > e5) and (e2 < e4):
            patterns["Broadening_Bottom"].append((window.index[0], window.index[-1]))

        # Triangle Top
        elif (e1 > e2) and (e1 > e3) and (e3 > e5) and (e2 < e4):
            patterns["Traingle_Top"].append((window.index[0], window.index[-1]))

        # Triangle Bottom
        elif (e1 < e2) and (e1 < e3) and (e3 < e5) and (e2 > e4):
            patterns["Traingle_Bottom"].append((window.index[0], window.index[-1]))

        # Rectangle Top
        elif (
            (e1 > e2)
            and (abs(e1 - rtop_g1) / rtop_g1 < 0.0075)
            and (abs(e3 - rtop_g1) / rtop_g1 < 0.0075)
            and (abs(e5 - rtop_g1) / rtop_g1 < 0.0075)
            and (abs(e2 - rtop_g2) / rtop_g2 < 0.0075)
            and (abs(e4 - rtop_g2) / rtop_g2 < 0.0075)
            and (min(e1, e3, e5) > max(e2, e4))
        ):
            patterns["RTOP"].append((window.index[0], window.index[-1]))

        # Rectangle Bottom
        elif (
            (e1 < e2)
            and (abs(e1 - rtop_g1) / rtop_g1 < 0.0075)
            and (abs(e3 - rtop_g1) / rtop_g1 < 0.0075)
            and (abs(e5 - rtop_g1) / rtop_g1 < 0.0075)
            and (abs(e2 - rtop_g2) / rtop_g2 < 0.0075)
            and (abs(e4 - rtop_g2) / rtop_g2 < 0.0075)
            and (max(e1, e3, e5) > min(e2, e4))
        ):
            patterns["RBOT"].append((window.index[0], window.index[-1]))

    return patterns


