import pandas as pd

data = {'a':25,'b':45,'c':65,'d':85}
series_dict = pd.Series(data)

print(series_dict)

data = [10,2,3,45,65]
series = pd.Series(data)
print(series)
#arithematical operation
 
series_add = series + 10
 
print(series_add)
 
# filter elemnts in the series.
 
filtered_series = series[series > 20]
print(filtered_series)
 
 
#statical method
#data = [10,2,3,45,65]
 
mean = series.mean()
print (f"the mean value of the series is {mean}")
