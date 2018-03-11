#
# Python Name: stockFunctions
# Progammer: Shing Chan
# Date Submitted: NaN
# Operating System: Windows

from datetime import datetime, timedelta
import pandas as pd
import pandas_datareader.data as web

#A modified function of web.DataReader with restricted time parameters (latest possible date) which displays all of
#each companies stock data in one DataFrame.
def getLatestStocks(companies, source, start, end):
    stockFrame = pd.DataFrame()
    for company in companies: #Will loop for each single company
        stockData = pd.DataFrame.reset_index(web.DataReader(company, source, start, end))
        #Gets the stock data from yesterday if there is no stock information for today:
        if stockExists(stockData):
            dayBefore = start - timedelta(days=1)
            stockData = pd.DataFrame.reset_index(web.DataReader(company, source, dayBefore, end))
        stockFrame = pd.concat([stockFrame, stockData])
    stockFrame.index = companies
    return(stockFrame)


def stockExists(stockData):
    return (stockData.dropna().empty) #DataFrames are techincally not "empty" if they have NaNs for their data

#def stockPrice(stockData):
    #return(stockData.iloc([0,0]))








