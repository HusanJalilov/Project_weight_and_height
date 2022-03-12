import csv

def read_csv_data(file_path):
    """
    Read csv file
    Args:
        file_path(str): file path
    Returns:
        list: data split row
    """
    s=file_path.split('\n')
    result_data=[]
    for i in s:
        result_data.append(i)
    
    
    # WRITE YOUR CODE HERE
    return result_data
file_path=open('data/weight-height.csv').read()
read_csv_data(file_path)

    