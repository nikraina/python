from pandas.io.parsers import _is_index_col

__author__ = 'nikhil'
import pandas as pd
from pandas import DataFrame

# df = pd.read_csv("sp500_ohlc.csv")    #right now the system doesnot know what is primary key here to mention it do::
df = pd.read_csv("sp500_ohlc.csv", index_col = "Date", parse_dates = True)
print df.head()