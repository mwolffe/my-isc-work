import numpy as np

arr = np.array([range(4), range (10,14)])

print(arr.shape)
print(arr.size)
print(arr.min())
print(arr.max())


print(np.reshape(arr, (2,2,2))) #reshape to 2,2,2
print(np.transpose(arr)) #flip to 2x4 from 4x2
print(np.ravel(arr)) #transpose to single dimension
print(arr.astype(np.float64)) #convert to float
