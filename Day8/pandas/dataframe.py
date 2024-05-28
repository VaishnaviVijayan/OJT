import pandas as pd

# dataframe with dict
data = {
    'Name':['kigini','tuttu','ikka'],
    'Age': [24,23,24],
    'Place':['Koovode','mavoor','punoor']
}

# convert to dataframe

df = pd.DataFrame(data)

#print(df)

#print(df[['Name','Place']])

#each row use inbuild fuc = iloc()
#print(df.iloc[1])

#print(df[df['Age'] > 23])

# add new column
#df['stipend'] = [15000,5000,5000]

#print(df)

#remove column

df= df.drop(columns=['Age'])

#discribe() helps 
print(df.describe())