# import numpy as np
# import scipy
# import pandas as pd
#import matplotlib as mp

"""
A classification example for machine learning using the iris dataset from scikit learn datasets
"""

from sklearn import datasets, linear_model

iris = datasets.load_iris()

print(iris.DESCR)

#inputs
features = iris.data
print("features of type: ", type(features))

#classifier -3 classes example
targets = iris.target

#preparing the model using inputs and targets
model = linear_model.LogisticRegression()
model.fit(features, targets)

#accuracy on the given test data and labels
print("score of the model: ", model.score(features, targets))

#prediction
model.predict(features[:1,:])

# next example is to split the available data into training, testing and validation

from sklearn import model_selection

X_train, X_test, y_train, y_test = model_selection.train_test_split(features,targets
                                                                    ,test_size=0.33, random_state=1)

model.fit(X_train, y_train)

print("score of the model with testdata: ", model.score(X_test, y_test))

y_predicted = model.predict(X_test)

print("predicted y: ", y_predicted)
print("actual test data y: ", y_test)

