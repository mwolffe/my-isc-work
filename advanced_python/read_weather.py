import netCDF4
import numpy as np

def read_header(file):
    
    """Reads the header of a simple CSV file and returns header as a dictionary"""

    with open(file) as file:
        Header = {}
        i = 0

        while i < 3:
            line = file.readline() #reads a line of the file
            line = line.strip() #strips white space
            key, value = line.split(':') #splits the line into a key and value
           
            header[key] = value #assigns the key to dictionary with associated value
            i += 1 #iterates through first three lines
        return header
        

#test
read_header(weather_meta.csv)
