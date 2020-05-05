import numpy as np

import csv
with open("/home/vipai/repos/some_code/Kaizen/datascience_ML_learning/dataquest_learning/numpy_tutorial/winequality-red.csv", 'r') as f:
    wines = list(csv.reader(f, delimiter=";"))
wines = np.array(wines[1:], dtype=np.float)

print(wines)

print("shape", wines.shape)

#wines = np.genfromtxt("winequality-red.csv", delimiter=";", skip_header=1)

print(np.random.rand(3))

print(wines[:,11] + 10)
print(wines[:,11])
