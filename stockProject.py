#
# Python Name: stockProject
# Progammer: Shing Chan
# Date Submitted: NaN
# Operating System: Windows

#
# Python Name: stockProject
# Progammer: Shing Chan
# Date Submitted: NaN
# Operating System: Windows


import datetime
import pandas_datareader.data as web
import stockFunctions

listAPI = ['google', 'fred', 'quandul', 'morningstar', 'famafrench', 'iex']
automaticMode = False
#automaticMode is an mode designed to automacially give stock prices for the current date. This is specifically designed for the developer who
# may simply only need the stock information while having already inputed the same default settings. Only changable in source code.
if automaticMode == False:
    #Ask DataReader Parameters:
    while True:
        setCompany = input("What company would you like? (In NASDAQ format only): ")
        setSource = input("What API would you like to use? Current valid APIs are google, iex, fred, quandl, morningstar, and famafrench:")
        setYear = int(input("What year? "))
        setMonth = int(input("What month? "))
        setDay = int(input("What day? "))
        setDate = datetime.datetime(setYear,setMonth,setDay)
        stockData = web.DataReader(setCompany, setSource, setDate, setDate)
        #Prints the name, and the worth of a share.
        print(str(setCompany) + ": $" + str(stockData.iloc[0,3]))
else:
    print("Automatic mode activated:")
    #Automatically intializes the datareader parameters
    currentTime = datetime.datetime.now()
    source = 'iex'
    currentDate = datetime.datetime(currentTime.year,currentTime.month,currentTime.day)
    cNames = ['AMZN', 'MSFT', 'NVDA', 'NKE', 'PEP']
    #Prints the respective stocks of each company.
    stockFunctions.latestStocks(cNames, source, currentDate, currentDate)


