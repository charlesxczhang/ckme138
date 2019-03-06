
from pandas_datareader import data as pdr
import datetime

import fix_yahoo_finance as yf
yf.pdr_override()

start = datetime.datetime(2018,1,1)
end = date.data.today()
baba =  pdr.get_data_yahoo('BABA', start, end)


import pandas as pd
from pandas



tech_list = ['AAPL','GOOG','AMZN','MSFT']
end = datetime.now()
start = datetime(end.year - 1)

for stock in tech_list:
	globals()[stock] =  pdr.get_data_yahoo(stock, start, end)





AAPL.decribe()
AAPL.info()


ma_day = [10,20,50]

for ma in ma_day:
	column.
	AAPL[] rollingmean



closing_df =  DataReader(['AAPL','GOOG','MSFT','AMZN'],'yahoo', start, end)['Adj close']





pip