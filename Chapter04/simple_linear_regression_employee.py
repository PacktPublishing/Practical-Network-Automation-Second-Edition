# Simple Linear Regression

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
empdata=pd.read_csv('employee_data.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 42)


# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


for item,row in empdata.iterrows():
    tmp=row['Exp']
    y_pred = regressor.predict(np.array([[tmp]]))
    status=""
    if (y_pred[0] <= row['Salary']):
        status="OverPaid"
    else:
        status="UnderPaid"
        
    print ("Name: %s , Exp: %s , Current Salary: %d , Predicted Salary: %d , Status: %s" % (row['Employee_Name'],row['Exp'],row['Salary'],y_pred[0],status))




