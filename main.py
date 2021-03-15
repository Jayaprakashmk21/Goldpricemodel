def function_linear(x, y):
 import pandas as pd
 dataset = pd.DataFrame()
 dataset['x'] = x
 dataset['y'] = y
 # Calculating mean of x,y

 x_mean = dataset['x'].mean()
 y_mean = dataset['y'].mean()

 print(x_mean)
 print(y_mean)

 # calculating x-x_mean and storing it in the same dataset

 dataset['x - x_mean'] = dataset['x'] - x_mean
 print(dataset)

 # calculating y-y_mean and storing it in the same dataset

 dataset['y - y_mean'] = dataset['y'] - y_mean
 print(dataset)

 # calculating (x - x_mean)^2 and storing it in the same dataset

 dataset['(x - x_mean)^2'] = dataset['x - x_mean'] * dataset['x - x_mean']
 print(dataset)

 dataset['(x - x_mean) * (y - y_mean)'] = dataset['x - x_mean'] * dataset['y - y_mean']
 print(dataset)

 # Formulating line equ. y = mx + c

 slope = dataset['(x - x_mean) * (y - y_mean)'].sum() / dataset['(x - x_mean)^2'].sum()
 intercept = y_mean - slope * x_mean
 print("Linear Regression model equ.: y = ", slope, "x + ", intercept)

 # calculating the estimated y values

 dataset['Est_y'] = (slope * dataset['x']) + intercept
 print(dataset)

 # calculating error to check the acceptance of the model

 dataset['y - Est_y'] = dataset['y'] - dataset['Est_y']
 print(dataset)

 dataset['(y - Est_y)^2'] = dataset['y - Est_y'] * dataset['y - Est_y']
 print(dataset)

 # calculating Mean Square Error and Root Mean Square Error

 import math

 mse = dataset['(y - Est_y)^2'].mean()
 rmse = math.sqrt(mse)
 print("MSE : ", mse, "\nRMSE :", rmse)

 # Visualisation
 # plotting x,y

 import matplotlib.pyplot as plt

 plt.scatter(dataset['x'], dataset['y'])
 plt.title("Visualising X, Actual Y")
 plt.show()

 #Line equation for the dataset

 plt.scatter(dataset['x'],dataset['y'])
 plt.plot(dataset['x'],dataset['Est_y'])
 plt.title("Equ. of line")
 plt.show()
 print("\nLinear Regression model equ.: y = ",slope,"x + ",intercept)
 print("MSE : ",mse,"\nRMSE :",rmse)

import pandas as pd
ds = pd.read_csv('/Users/admin/Desktop/goldprice.csv')
#print(dataset)
a = ds['x']
b = ds['y']
#print(a,b)
#print(b)
function_linear(a,b)