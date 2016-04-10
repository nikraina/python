__author__ = 'nikhil'

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

df = pd.read_csv("sp500_ohlc.csv",index_col = "Date")

df["H-L"] = df.High - df.Low #can also be accessed as df["High"]
df["100MA"] = pd.rolling_mean(df["Close"],100,min_periods = 1)
df["Diff"] = df["Close"].diff()

df["STD"] = pd.rolling_std(df["Close"],25, min_periods = 1)

print df.head()

plt1 = plt.subplot(2,1,1)
df["Close"].plot()

plt2 = plt.subplot(2,1,2,sharex = plt1)
df["STD"].plot()

plt.show()
