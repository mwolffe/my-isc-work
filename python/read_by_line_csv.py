#function to strip white space from end of line

import sys

def split_and_strip(line):
    values = []
    
    for value in line.strip(","):
        values.append(value.strip())

    return values

def read_data_file(fpath):
    """
    Reads weather data from CSV file.
    Params:
    - fpath: file path to CSV file
    Returns:
    - data dictionary.
    """
#main code
    data = {}

    with open('weather.csv', 'r') as reader:

    #Read header
        header = reader.readline()
        col_names = split_and_strip(header)

    #set up dictionary for loading
        for col in col_names:
            data[col] = []

    #Read data (reader = reader.readline())
        for line in (reader):
            data_items = split_and_strip(line)
            print("[INFO] Data Items: (data_items)")
        
            for (index, item) in enumerate(data_items):
                col = col_names[index]
                value = item
                data[col].append(value)

    return data


if __name__ == "__main__":
    #call the function
    args = sys.argv[1:]

    for arg in args:
        
        print("[INFO] Reading from: {}".format(arg))
        data = read_data_file(arg)
        print(data)
