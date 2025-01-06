import numpy as np
import matplotlib.pyplot as plt

def myconv(h, x):
    hlength = len(h)
    xlength = len(x)
    ylength = hlength + xlength - 1
    hh = np.hstack([h, np.zeros(xlength - 1)])
    xx = np.hstack([x, np.zeros(hlength - 1)])
    y = np.zeros(ylength)
    for n in range(0, ylength): 
        for k in range(0, n + 1): 
            y[n] += hh[k] * xx[n - k]
    return y

h = np.array([1,3,-1])
x  = np.array([2,1,5,3])
y = myconv(h,x)
print("y = ",y)