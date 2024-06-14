import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#dataset
height = np.array([150,160,164,165,173]).reshape(-1,1)
weight = np.array([50,60,63,68,72]) 

#linar regression model for dataset
model = LinearRegression()

#fit the model with data

model.fit(height,weight)

predicted_weight = model.predict(height)

print(f"intercept: {model.intercept_}")
print(f"coefffiecents: {model.coef_[0]}")

#scatterplot

plt.scatter(height,weight,color='blue')
plt.plot(height,predicted_weight,color='red')
plt.xlabel('height')
plt.ylabel('weight')
plt.title('linear regression')
plt.show()

