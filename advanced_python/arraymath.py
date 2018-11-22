import numpy as np

def calcmagnitude(u, v, minmag = 0.1):
    mag = ((u ** 2) + (v ** 2)) ** 0.5
    output = np.where(mag > minmag, mag, minmag)
    return output

u = np.array([[4,5,6], [0,21,0.02]])
v = np.array([[2,2,2], [1,1,1]])

print(calcmagnitude(u,v))
