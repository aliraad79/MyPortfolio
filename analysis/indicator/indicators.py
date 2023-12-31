import pandas_ta as ta


def add_bbands(df):
    df.ta.bbands(append=True)


def add_sma(df, period=10):
    df.ta.sma(period, append=True)


def add_rsi(df, period=14):
    df.ta.rsi(period, append=True)


def add_adx(df, length=14):
    df.ta.adx(length=length, append=True)


def add_cci(df, length=20):
    df.ta.cci(length, append=True)


def add_macd(df, fast=12, slow=26, signal=9):
    df.ta.macd(fast=fast, slow=slow, signal=signal, append=True)


def add_ichimoku_cloud(df):
    df.ta.ichimoku(append=True)


def add_smas(df):
    add_sma(df, 5)
    add_sma(df)
    add_sma(df, 20)
    add_sma(df, 50)
