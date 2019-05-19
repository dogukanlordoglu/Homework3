# IHSAN DOGUKAN LORDOGLU AND KAMRAN HUSEYNOV (COLLABORATED)
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def drawCharts(timeseries, windowSize):
    #Determing rolling statistics
    rolmean = pd.Series(timeseries).rolling(window=windowSize).mean()
    rolstd = pd.Series(timeseries).rolling(window=windowSize).std()
    #Plot rolling statistics:
    orig = plt.plot(timeseries, color='blue',label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)

# Load data
df = pd.read_csv("data.csv", sep='\t')
#print(df_volume_not_zero)
seriesname = 'Open'
series = df[seriesname]
drawCharts(series, df.size)
seriesname = 'Close'
series = df[seriesname]
drawCharts(series, df.size)
seriesname = 'High'
series = df[seriesname]
drawCharts(series, df.size)
seriesname = 'Low'
series = df[seriesname]
drawCharts(series, df.size)


#data = pd.read_pickle('./data.pkl')
#original = pd.read_csv("data.csv", sep='\t')
#df = original.head(len(original)-1)

#print(df)

# Function for Moving Average
#def estimate_moving_average(df,seriesname,windowsize):
#    avg = df[seriesname].rolling(windowsize).mean().iloc[-1]
#    return avg
#
#days = 11040 # observed period is 11040 days
#name='Open'
#movingaverageofopen = round(estimate_moving_average(df,name, days),0)
#print("Moving average of open estimation for last ", days, " days: ", movingaverageofopen)
#name='Close'
#movingaverageofclose = round(estimate_moving_average(df,name, days),0)
#print("Moving average of close estimation for last ", days, " days: ", movingaverageofclose)
#name='High'
#movingaverageofhigh = round(estimate_moving_average(df,name, days),0)
#print("Moving average of high estimation for last ", days, " days: ", movingaverageofhigh)
#name='Low'
#movingaverageoflow = round(estimate_moving_average(df,name, days),0)
#print("Moving average of low estimation for last ", days, " days: ", movingaverageoflow)

#cols = ['Open', 'High', 'Low', 'Close', 'Volume']
#print(data["Day"])
#print(data.info())

#for col in cols:
    #print(col)
    #data[col] = data[col].astype(float)
    #print(data[col])
#data.head(10)

#short_rolling = data.rolling(window=20).mean()
#short_rolling.head(20)

#long_rolling = data.rolling(window=100).mean()
#long_rolling.tail()

#start_date = '29.04.2019'
#end_date = '6.05.2019'

#fig, ax = plt.subplots(figsize=(16,9))

#ax.plot(data.loc[start_date:end_date, :].index, data.loc[start_date:end_date, 'Open'], label='Open')
#ax.plot(long_rolling.loc[start_date:end_date, :].index, long_rolling.loc[start_date:end_date, 'MSFT'], label = '100-days SMA')
#ax.plot(short_rolling.loc[start_date:end_date, :].index, short_rolling.loc[start_date:end_date, 'MSFT'], label = '20-days SMA')

#ax.legend(loc='best')
#ax.set_ylabel('Price in $')
#ax.xaxis.set_major_formatter(my_year_month_fmt)