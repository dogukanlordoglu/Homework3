#IHSAN DOGUKAN LORDOGLU AND KAMRAN HUSEYNOV COLLABORATED
#3A#smoothing by A simple (one-sided) moving average

df = df.set_index(["Day","Time"])
smoothed_data = df.rolling(window=60).mean()
smoothed_data = smoothed_data.dropna()
#print(smoothed_data.head(61))
calculate_everything(smoothed_data)
df = df.reset_index(["Day","Time"])

seriesname = "Close"
series = df[seriesname]
test_stationarity(series)
print(series.tail())

###3C One random (representative) pick from each hour
df2 = (df.sample(n= 10))
calculate_everything(df2)
seriesname = "Close"
series = df2[seriesname]
test_stationarity(series)
print(series.tail())