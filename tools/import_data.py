import os , csv
from sklearn import datasets
import numpy as np

def load_dataset(source_file = ''):
    with open(source_file) as f:
        ncols = len(f.readline().split(','))
    faetures_set = np.loadtxt(source_file, delimiter=",", skiprows=1,usecols=range(2, ncols - 1))
    lable_set = np.loadtxt(source_file, dtype='str', delimiter=",", skiprows=1, usecols=range(ncols))
    return faetures_set , lable_set