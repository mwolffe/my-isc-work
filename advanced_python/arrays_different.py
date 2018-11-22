import numpy as np

a = np.zeros((2,3,4), dtype=np.float64) #Given in z,y,x format
b = np.ones((2,3,4), dtype=np.float64)

#print(a)
#print(b)

c = np.arange(1000)
#print(c)

d = [2, 3.2,5.5, -6.4, -2.2, 2.4]

d1 = np.array(d, dtype = np.float64)
#print( d1[1:4] )

e = [[2, 3.2,5.5, -6.4, -2.2, 2.4], [1, 22, 4, 0.1, 5.3, 9], [3, 1, 2.1, 21, 1.1, -2]]

e1 = np.array(e, dtype = np.float64)
#print(e1)

#print(e1[:,3]) #prints 3rd index column
#print(e1[1:4, 0:4]) #prints 1-4 index rows and 0-4 index columns
#print(e1[1:, 2]) #prints all index rows from 1 at index column 2

