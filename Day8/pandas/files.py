import pandas as pd

dp= pd.read_csv("data.csv"),(
                dtype = {'Age':int,'Salary':float}
                usecols = ['Name','Age,','Place'])
print(df)