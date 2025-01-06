import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# def mydft2(nyu):
#     return nyu

f = 3
fs = 20
t = np.arange(0, 2, 1/fs)
fk = np.arange(0, fs, fs/(2*fs))
sig = np.sin(2*np.pi*f*t)
fsig = mydft2(sig)
plt.subplot(2,1,1)
plt.plot(t,sig)
plt.xlabel('Time [sec]')
plt.ylabel('x(t)')
plt.grid()
plt.subplot(2,1,2)
plt.plot(fk, abs(fsig))
plt.xlabel('Frequency [Hz]')
plt.ylabel('|X(f)|')
plt.grid()


