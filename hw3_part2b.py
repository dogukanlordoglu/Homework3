#IHSAN DOGUKAN LORDOGLU AND KAMRAN HUSEYNOV (COLLABORATED)
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def estimate_holt(df, seriesname, alpha=0.2, slope=0.1, trend="add"):
    numbers = np.asarray(df[seriesname], dtype='float')
    model = Holt(numbers)
    fit = model.fit(alpha, slope, trend)
    estimate = fit.forecast(1)[-1]
    return estimate

def decomp(frame,name,f,mod='Additive'):
    #frame['Date'] = pd.to_datetime(frame['Date'])
    series = frame[name]
    array = np.asarray(series, dtype=float)
    result = sm.tsa.seasonal_decompose(array,freq=f,model=mod,two_sided=False)
    # Additive model means y(t) = Level + Trend + Seasonality + Noise
    result.plot()
    plt.show() # Uncomment to reshow plot, saved as Figure 1.
    return result


# Load data
df = pd.read_csv("data.csv", sep='\t')
df = df[df.time[2:] == '59' || df.time[2:] == '00']
seriesname = 'Open'

print("Method 1 - dropna()")
df2 = df.dropna()
result = decomp(df2,seriesname,f=52) # 52 weeks per year
# Estimate 'Open' for next 1 period
open = round( estimate_holt(df2, seriesname, alpha=0.2, slope=0.1, trend="add"), 2)
print("Estimation on open:", open)

print("Method 2 - fillna")
# Load data
df = pd.read_csv("data.csv", sep='\t')
df = df[df.time[2:] == '59' || df.time[2:] == '00']
# forward fill, propagate non-null values forward
df3 = df.fillna(method ='ffill')
# backward fill, propagate non-null values backward
df3 = df3.fillna(method ='bfill') 
result = decomp(df3,seriesname,f=52)

open = round( estimate_holt(df3, seriesname, alpha=0.2, slope=0.1, trend="add"), 2)
print("Estimation on open:", open)


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