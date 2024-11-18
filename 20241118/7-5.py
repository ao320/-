import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t = np.arange(0, 1, 0.001)
fs = 15
nt = np.arange(0, 1, 1/fs)
x = 2 + np.cos(10*np.pi*t) + 2*np.cos(20*np.pi*t) + np.cos(30*np.pi*t)
plt.plot(t,x)
xs = 2 + np.cos(10*np.pi*nt) + 2*np.cos(20*np.pi*nt) + np.cos(30*np.pi*nt)
plt.plot(nt,xs,"ro")
xa = 3 + 3*np.cos(10*np.pi*t)
plt.plot(t,xa,color="orange")
plt.grid()
plt.xlabel('t [sec]')
plt.show()