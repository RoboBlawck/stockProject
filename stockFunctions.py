#
# Python Name: stockFunctions
# Progammer: Shing Chan
# Date Submitted: NaN
# Operating System: Windows

import datetime
import pandas_datareader.data as web

def latestStocks(list, source, start, end):
        # Attempts to display the stocks of the current days.
        for n in range(0, len(list)): #Will loop for each single company because of len(list)
            stockData = web.DataReader(list[n], source, start, end)
            #Countermeasures incase stock information of current date is not published yet, will instead go back one day.
            if stockData.empty:
                currentTime = datetime.datetime.now()
                start = datetime.datetime(currentTime.year, currentTime.month, currentTime.day - 1)
                end = datetime.datetime(currentTime.year, currentTime.month, currentTime.day)
                stockData = web.DataReader(list[n], source, start, end)
            print(str(list[n]) + ": $" + str(stockData.iloc[0, 3]))
            #Developer notes: Normally I would have done something to make this return a list, but this project doesn't require that.
