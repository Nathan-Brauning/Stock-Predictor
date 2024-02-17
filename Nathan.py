

import yfinance as yf
from datetime import datetime, timedelta

x_days_ago = 14

end_date = datetime.now() 

start_date = end_date - timedelta(days=x_days_ago)

print(end_date)

print(start_date)

#Replace "AMZN" with the stock input
stock = yf.Ticker("AMZN")

stock_history = stock.history(start=start_date, end=end_date)

#Doesn't work now? ;(
print(stock_history)


