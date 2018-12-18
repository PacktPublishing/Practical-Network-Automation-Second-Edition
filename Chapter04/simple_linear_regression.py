# Simple Linear Regression

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

####print the data list
print ("Years of Experience in CSV...")
print (X)
print ("Salary based upon of Experience in CSV...")
print (y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 42)


# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


###Predict certain salary for the experience years
y_pred = regressor.predict(np.array([[15]]))
print ("\n\nPredicted salary for 15 years of experience:")
print (y_pred)


y_pred = regressor.predict(np.array([[25]]))
print ("\n\nPredicted salary for 25 years of experience:")
print (y_pred)

y_pred = regressor.predict(np.array([[13]]))
print ("\n\nPredicted salary for 13 years of experience:")
print (y_pred)



 #Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

