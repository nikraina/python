__author__ = 'nikhil'
import pandas as pd
from pandas import DataFrame

df = pd.read_csv("sp500_ohlc.csv", index_col = "Date", parse_dates = True)

df1 = df["Open"]
print df1.head()

#when you want more than one column from the previous df
df2 = df[["Open", "Close"]]
print df2.head()

df3 = df2[(df2["Close"]>1400)]
print df3

df2.rename(columns={"Close":"CLOSE"}, inplace = True)
print df2.head()

del df2["CLOSE"]    #delete the column from dataframe
print df2.head()