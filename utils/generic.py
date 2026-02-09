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


def get_column_from_csv(file_path, column_name):
    df = pd.read_csv(file_path)

    return df[column_name]

result = get_column_from_csv('E:\Downloads\ archive (2)\world_university_survey_dataset.csv', 'age')
print(result)
print(array_average(result))
print(min_max_array(result))