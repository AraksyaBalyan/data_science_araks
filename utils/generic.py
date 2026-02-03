import pandas as pd

def read_file_pandas(filename):
    csv_file_data = pd.read_csv(filename)
    return csv_file_data

