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

f = 3
fs = 1000
N = 2048
t = np.arange(0, N/fs, 1/fs)
sig = np.sin(2*np.pi*f*t) + np.random.randn(N)
h = np.array([0.33, 0.33, 0.33])
fdsig = myconv(h, sig)
plt.subplot(2,1,1)
plt.plot(t,sig)
plt.xlabel('Time [sec]')
plt.ylabel('Original')
plt.grid()
plt.subplot(2,1,2)
plt.plot(t, fdsig[:N])
plt.xlabel('Time [sec]')
plt.ylabel('Filtered')
plt.grid()