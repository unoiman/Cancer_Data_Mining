import os
from sklearn import datasets
import numpy as np
curfilePath = os.path.abspath(__file__)
# this will return current directory in which python file resides.
curDir = os.path.abspath(os.path.join(curfilePath, os.pardir))
# this will return parent directory.
parentDir = os.path.abspath(os.path.join(curDir, os.pardir))
print (parentDir)
# iris = datasets.load_iris()
# digits = datasets.load_digits()
test_set = np.loadtxt(open("test.csv", "rb"), delimiter=",", skiprows=1)
print(test_set.shape)