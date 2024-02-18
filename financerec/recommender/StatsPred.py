'''
Taking Nate's statistical stuff in Jupyter and making it into a 
class so it's easier to import and do shit with
'''

import statistics as stats
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

import json 

class StatsPred():
    def __init__(self, x_days_before, ticker):
        self.end_date = datetime.now()
        self.start_date = self.end_date - timedelta(days=x_days_before)
        self.ticker = ticker

    def retrieve_history(self):
        # Using the yfinance library to find the stock history
        stock = yf.Ticker(self.ticker)
        return stock.history(start=self.start_date)
    
    def retrieve_values_as_json(self):

        history = StatsPred.retrieve_history()

        closing_prices = history['Close'].tolist()
        num_days = len(history)

        '''Performing statistical calculations on the closing prices for the past x days, 
        converting it to a json, and then returning it'''

        # SD
        standard_deviation = stats.stdev(closing_prices)

        x_values = []
        i = 1
        while i <= num_days:
            x_values.append(i)
            i += 1 

        # finding coordinates and comparing them with closing prices
        graph_coordinates = zip(x_values, closing_prices)

        # finding the slope and intercept of the model
        slope, intercept = stats.linear_regression(x_values, closing_prices)

        # Finding percent change from current price ot 
        percent_change = (closing_prices[num_days -1] - closing_prices[0]/closing_prices[0]*100)

        if (closing_prices[num_days - 1] - closing_prices[0]) / closing_prices[0] > 0.1 / (365/self.x_days_before):
            should_invest = True
        else:
            should_invest = False

        # This is where tthe json
        statistics = {"closing_prices": closing_prices,
                    "standard_deviation": standard_deviation,
                    "graph_coordinate": tuple(graph_coordinates),
                    "slope": slope,
                    "intercept": intercept,
                    "percent_change": percent_change,
                    "should_invest?": should_invest}

        return json.dumps(statistics)
            




