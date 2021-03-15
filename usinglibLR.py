import pandas as pd

dataset = pd.read_csv('/Users/admin/Desktop/goldprice.csv')
print(dataset)

x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2:3].values

from sklearn.linear_model import LinearRegression

model1 = LinearRegression()

model1.fit(x, y)

slope = model1.coef_
intercept = model1.intercept_
print("Equ. of line y= ", slope, "x + ", intercept)

import matplotlib.pyplot as plt

new_X = [[1810]]
new_y = model1.predict(new_X)
plt.scatter(x, y, color='red')
plt.plot(x, model1.predict(x), color='blue')
plt.scatter(new_X, new_y, color='black', marker='*')
plt.title('gold prediction')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
