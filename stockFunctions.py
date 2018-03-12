#
# Python Name: stockFunctions
# Progammer: Shing Chan
# Date Submitted: NaN
# Operating System: Windows

from datetime import datetime
import pandas as pd
import pandas_datareader.data as web

#A modified function of web.DataReader with restricted time parameters (latest possible date) which displays all of
#each companies stock data in one DataFrame.
def getStocks(companies, source, dates):
    stockFrame = pd.DataFrame()
    dates = list(filter(lambda date: date < datetime.now(), dates)) #Filters out the dates in the future
    for company in companies: #Will loop for each single company
        for date in dates:
            stockData = pd.DataFrame.reset_index(web.DataReader(company, source, date, date))
            stockData.index = [company]  # reset_index cannot be used with index = at the same time
            stockFrame = pd.concat([stockFrame, stockData])
    stockFrame['date'] = pd.to_datetime(stockFrame.date)
    stockFrame = stockFrame.sort_values(by='date')
    return(stockFrame)

def latestStocks(stockFrame):
    return (stockFrame.tail(5)) #When the stockFrame is sorted with ascending = true, last n rows of stockFrame is the
#latest stock information, assume n=5

def latestShares(investments, stockFrame):
    stockPrices = stockFrame['close']#Gets stock prices
    stockPrices.index = stockFrame.index #<- Ineffiecent method to index
    #shares = list(map(calculateShares, stockPrices, investments)) #Calculates the share for each respective company
    investments = pd.Series(investments)
    shares = stockPrices.apply(calculateShares, args=(investments, ))
    shares = shares[0]
    stockFrame = stockFrame.assign(shares=shares) #Assigns data to DataFrame
    investments.index = stockFrame.index # shares = shares[0] hinges on this command being after it
    stockFrame = stockFrame.assign(investments=investments)
    return(stockFrame)

def calculateShares(stockPrice,investment):
    return(investment/stockPrice)

#Function to check if there is any stock information in the DataFrame
def stockExists(stockData):
    return (not stockData.dropna().empty) #DataFrames are techincally not "empty" if they have NaNs for their data

def loadStock(stockFrame): #Only works with one row
    return(stockFrame.iat[0,3])









