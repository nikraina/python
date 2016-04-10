__author__ = 'nikhil'

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

df = pd.read_csv("sp500_ohlc.csv",index_col = "Date")

df["H-L"] = df.High - df.Low #can also be accessed as df["High"]

print df.describe() #gives you the basic stats information

print df.corr() #gives you the corelation of each column against each other

print df.cov() #gives you the covariance of each column against each other
