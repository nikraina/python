__author__ = 'nikhil'

import pandas as pd
from pandas import DataFrame
import datetime
import pandas.io.data

sp500 = pd.io.data.get_data_yahoo('%5EGSPC',
                                  start=datetime.datetime(2000,10,1),
                                  end=datetime.datetime(2016,1,1))

#print sp500
#to just get the idea of data use head()
print sp500.head()
sp500.to_csv("sp500_ohlc.csv")
