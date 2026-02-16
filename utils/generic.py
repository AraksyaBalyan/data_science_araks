import pandas as pd
import numpy as np


def read_file_pandas(filename, columns):
    try:
        csv_file_data = pd.read_csv(filename)
    except KeyError:
        print("KeyError: Column->", list(csv_file_data.columns), f"Provided -> {columns}")
        return None
    except FileNotFoundError:
        print("Message-> ")


def array_average(arr):
    return np.average(arr)


def min_max_array(arr):
    minimum = arr.min()
    maximum = arr.max()
    return minimum, maximum


def get_column_from_csv(file_path, column_name):
    df = pd.read_csv(file_path)

    return df[column_name]


def print_column_names(df):
    for col in df.columns:
        return f"column names are - {col}"


def print_basic_info(df):
    return df.info()


def analyze_missing_values(df):
    missing_data = df.isnull().sum()
    if missing_data.sum() == 0:
        return "All cells are filled (there are no missing values)."
    else:
        return "missing_data[missing_data > 0]"
