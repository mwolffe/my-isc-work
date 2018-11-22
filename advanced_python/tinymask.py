import numpy.ma as MA
import numpy as np

m1 = MA.masked_array(range(1,9))
print(m1)

m2 = MA.reshape(m1, (2, 4))
print(m2)

m3 = MA.masked_greater(m2, 6)
print(m3)

print(100*m3)

res = m3 - np.ones((2,4))
print(res)
