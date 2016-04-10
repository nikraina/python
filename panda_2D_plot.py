__author__ = 'nikhil'

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

df = pd.read_csv("sp500_ohlc.csv",index_col = "Date")

df["H-L"] = df.High - df.Low #can also be accessed as df["High"]
df["100MA"] = pd.rolling_mean(df["Close"],100)
df["Diff"] = df["Close"].diff()

# df.plot()   #plots all the columns
#we can plot individual coulmns as well
df["High"].plot()
plt.show()
