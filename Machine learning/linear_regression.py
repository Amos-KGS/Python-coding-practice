# Linear regression model to predict student score based on previous results.
# Special mention: TechWithTim
import sklearn
import tensorflow as tf
import keras as kt
import sklearn as sk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("student-mat.csv", sep=";")
# print(data.head())
data = data[["G1", "G2", "G3", "freetime", "goout", "absences"]]
# print(data)
predict_output = "G3"

x = np.array(data.drop([predict_output], 1))
y = np.array(data[predict_output])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y, test_size = 0.2)

linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)

accuracy_score = linear.score(x_test, y_test)
print(accuracy_score)

print("Coefficient: \n ", linear.coef_)
print("intercept: \n", linear.intercept_)

predictions_output = linear.predict(x_test)

for x in range(len(predictions_output)):
    print(predictions_output[x], x_test[x], y_test[x])
