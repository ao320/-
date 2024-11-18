import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 10
T = 1 / fs
f0 = 3
n = np.arange(0, 10)
x = np.sin(3 * n * np.pi / 5)
plt.stem(n * T,x,linefmt="red")
t = np.arange(0, 1, 0.001)
xa = np.sin(2 * t * np.pi * f0)
plt.plot(t,xa)
plt.grid()
plt.xlabel('t[sec]')
plt.show()