import datetime
import matplotlib.pyplot
from matplotlib import style
import pandas
import pandas_datareader.data as web

#Initilization started#
style.use('ggplot')
currentTime = datetime.datetime.now()
#Only works for up to 5 years#
source = 'iex'
start = datetime.datetime(2017,1,1)
end = datetime.datetime(currentTime.year,currentTime.month,currentTime.day)
companyData_1 = web.DataReader(company, source, start, end)
companyData_2 = web.DataReader(company, source, start, end)
#Initilization ended#

TESTs