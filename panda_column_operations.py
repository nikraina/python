__author__ = 'nikhil'

import pandas as pd
from pandas import DataFrame

df = pd.read_csv("sp500_ohlc.csv")

df["H-L"] = df.High - df.Low #can also be accessed as df["High"]
print df.head()

df["100MA"] = pd.rolling_mean(df["Close"],100)
print df[200:220]

df["Diff"] = df["Close"].diff()
print df.head()