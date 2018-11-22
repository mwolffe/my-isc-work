import numpy as np

x = list(range(1,11))

a = np.zeros((3,2), dtype=np.float64) #creates a 64 bit 3x2 array of zeros 

a1 = np.array(x, dtype=np.int32) #converts a list to an array of integers
a2 = np.array(x, dtype=np.float64)#converts a list to an array of floats

#print(x.dtype) - doesn't work as this is a list not an array
print(a1)
print(a1.dtype)
print(a2)
print(a2.dtype)

