import numpy as np
a = np.array([range(4), range(10,14)])

b = np.array([2, -1, 1, 0])
#print(a)
#print(b)
#print(a*b)

b1 = b*100
b2 = b*100.0

print(b1)
print(b2)
print(b1 == b2)
print(b1.dtype, b2.dtype)
