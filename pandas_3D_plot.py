__author__ = 'nikhil'

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv("sp500_ohlc.csv")

df["H-L"] = df.High - df.Low #can also be accessed as df["High"]
df["100MA"] = pd.rolling_mean(df["Close"],100)
df["Diff"] = df["Close"].diff()

threed = plt.figure().gca(projection = "3d")
threed.scatter(df.index,df["H-L"], df["Close"])
threed.set_xlabel("Index")
threed.set_ylabel("H-L")
threed.set_zlabel("Close")
plt.show()
