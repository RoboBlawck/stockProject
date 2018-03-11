#
# Python Name: stockProject
# Progammer: Shing Chan
# Date Submitted: NaN
# Operating System: Windows

from datetime import datetime
import pandas_datareader.data as web
import stockFunctions

listAPI = ['google', 'fred', 'quandul', 'morningstar', 'famafrench', 'iex']
automaticMode = True
#automaticMode is an mode designed to automacially give stock prices for the current date. This is specifically designed
#for the developer who # may simply only need the stock information while having already inputed the same default
#settings. Only changable in source code.
if automaticMode == False:
    #Ask DataReader Parameters:
    while True:
        company = input("What company would you like? (In NASDAQ format only): ")
        source = input("What API would you like to use? Current valid APIs are google, iex, fred, quandl, morningstar, "
                       "and famafrench:")
        year = int(input("What year? "))
        month = int(input("What month? "))
        day = int(input("What day? "))
        #price = float(input("What price would you like to mantain?"))
        date = datetime(year, month, day)
        #Gets stock data, indexes the company, and prints it.
        stockData = web.DataReader(company, source, date, date)
        stockData.index = [company]
        #share = price/stockFunctions.stockPrice(stockData)
        print(stockData)
        #print("The required shares to mantain $"+str(price)+"is: "+share+" shares")

else:
    print("Automatic mode activated:")
    #Automatically intializes the datareader parameters
    today = datetime.now()
    source = 'iex'
    companies = ['AMZN', 'MSFT', 'NVDA', 'NKE', 'PEP']
    stockData = stockFunctions.getLatestStocks(companies, source, today, today)
    print(stockData)




