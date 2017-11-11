import os , csv
from sklearn import datasets
import numpy as np
curfilePath = os.path.abspath(__file__)
# this will return current directory in which python file resides.
curDir = os.path.abspath(os.path.join(curfilePath, os.pardir))
# this will return parent directory.
parentDir = os.path.abspath(os.path.join(curDir, os.pardir)) #use to load the CSV files

# iris = datasets.load_iris()
# digits = datasets.load_digits()
with open(parentDir + '/trin-SD01/trin-SD01.csv') as f:
    ncols = len(f.readline().split(','))
faetures_test_set = np.loadtxt(parentDir + '/trin-SD01/trin-SD01.csv' , delimiter=",", skiprows=1 , usecols=range(2,ncols-1))
lable_test_set = np.loadtxt(parentDir + '/trin-SD01/trin-SD01.csv' ,dtype='str', delimiter=",", skiprows=1 , usecols=range(ncols))
print(lable_test_set.shape)
print(lable_test_set)