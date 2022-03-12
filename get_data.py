from read_data import read_csv_data


def get_data(data):
    """
    Get data from list.
    Gender: Change Male to 0 and Female to 1
    Weight: Place the column in the Kg view given in Pound (1 kg = 2,205 pound).
    Height: Place the column on the list in the cm view given in inches (2.54 cm = 1 inch).
    Args:
        data(list): data split row
    Returns:
        tuple: gender, weight and height

    """
    gender = []
    weight = []
    height = []
    
    # WRITE YOUR CODE HERE
    #print(data_result)
    #print(data)
    col=[]
    data1=data.split('\n')

    for i in range(len(data1)):
        for col in data[i].values():
            if val == 'Male':
                gender.append(0)
            elif val == 'Female':
                gender.append(1)


        for k in data[i].keys():
            if k == 'Height':
                height.append(float(data[i][k])/2.54)
            if k == 'Weight':
                weight.append(float(data[i][k])*2.205)
       

    return gender,weight,height
