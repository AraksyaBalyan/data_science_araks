import pandas as pd
import numpy as np

def read_file_pandas(filename):
    csv_file_data = pd.read_csv(filename)
    return csv_file_data


def array_average(arr):
    return np.average(arr)

def min_max_array(arr):
    minimum = arr.max()
    maximum = arr.min()
    return minimum, maximum