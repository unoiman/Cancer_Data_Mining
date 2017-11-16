import os , csv
from sklearn import datasets
import numpy as np
# import pandas as pd
def load_dataset(source_file = ''):
    with open(source_file) as f:
        data = f.readlines()[1]
        data = data.split(',')
        ncols = len(data)
        # print (data[ncols-1])
    lable_set = np.genfromtxt(source_file, delimiter=",", skip_header=1, usecols= ncols -1 , dtype=str ,max_rows=3)
    names_set = np.genfromtxt(source_file, delimiter=",", skip_header=1, usecols= 0 , dtype=str,max_rows=3 )
    faetures_set = np.genfromtxt(source_file, delimiter=",",skip_header=1, usecols=range(1, ncols - 2),max_rows=3)
    return faetures_set , lable_set ,names_set