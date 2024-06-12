import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the Excel file
file_path = 'weather_data.xlsx'  
df = pd.read_excel(file_path)

# Display the DataFrame
print(df)

# Handle missing values
df = df.dropna()

# Convert Date column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Calculate statistics for Temperature
temperature_mean = np.mean(df['Temperature'])
temperature_std = np.std(df['Temperature'])
temperature_max = np.max(df['Temperature'])
temperature_min = np.min(df['Temperature'])

print(f"Mean Temperature: {temperature_mean}")
print(f"Standard Deviation of Temperature: {temperature_std}")
print(f"Maximum Temperature: {temperature_max}")
print(f"Minimum Temperature: {temperature_min}")

# Time series plot for temperature
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Temperature'], marker='o', linestyle='-', color='g')
plt.title('Temperature Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

# Bar chart for average monthly precipitation
df['Month'] = df['Date'].dt.month
monthly_precipitation = df.groupby('Month')['Precipitation'].mean()

plt.figure(figsize=(10, 5))
monthly_precipitation.plot(kind='bar', color='c')
plt.title('Average Monthly Precipitation')
plt.xlabel('Month')
plt.ylabel('Precipitation (mm)')
plt.xticks(ticks=range(len(monthly_precipitation.index)), labels=[f"Month {i}" for i in monthly_precipitation.index])
plt.grid(True)
plt.show()

# Scatter plot for wind speed vs. temperature
plt.figure(figsize=(10, 5))
plt.scatter(df['WindSpeed'], df['Temperature'], color='b')
plt.title('Wind Speed vs. Temperature')
plt.xlabel('Wind Speed (km/h)')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()
