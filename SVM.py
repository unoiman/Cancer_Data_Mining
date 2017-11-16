import os , csv
from sklearn import datasets
import numpy as np
from tools.import_data import *
curfilePath = os.path.abspath(__file__)
# this will return current directory in which python file resides.
curDir = os.path.abspath(os.path.join(curfilePath, os.pardir))
# this will return parent directory.
parentDir = os.path.abspath(os.path.join(curDir, os.pardir)) #use to load the CSV files

faetures_test_set , lable_test_set = load_dataset(parentDir + '/trin-SD01/trin-SD01.csv')
print(lable_test_set.shape)
print(lable_test_set)