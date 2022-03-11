import csv

def read_csv_data(file_path):
    """
    Read csv file
    Args:
        file_path(str): file path
    Returns:
        list: data split row
    """
    #result_data =file_path.split(/n)
    print(type(file_path))
    result_data=file_path.split('\n')
    
    
    # WRITE YOUR CODE HERE
    return result_data
file_path=open('data/weight-height.csv').read()
print(read_csv_data(file_path))

    