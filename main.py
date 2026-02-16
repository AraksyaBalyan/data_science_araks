from utils.generic import get_column_from_csv, min_max_array, array_average, print_column_names, print_basic_info,analyze_missing_values, read_file_pandas

while True:
    file_name = input("Input data")
    column_name = input("Input column name")
    result = get_column_from_csv(file_name, column_name)
    print(result)
    print(array_average(result))
    print(min_max_array(result))
    data = read_file_pandas(file_name)
    print(print_column_names(data))
    print(print_basic_info(data))
    print(analyze_missing_values(data))
    if file_name == "break":
        print("Program end")
        break