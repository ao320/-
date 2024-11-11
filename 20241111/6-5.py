import numpy as np
import matplotlib.pyplot as plt
f = 5
fs = 10
t = np.arange(0, 1, 0.001)
x = np.sin(2*np.pi*f*t)
ts = np.arange(0, 1, 1/fs)
xs = np.sin(2*np.pi*f*ts)
plt.plot(t, x)
plt.stem(ts, xs, linefmt="red")
plt.grid()
plt.xlabel('Time [sec]')
plt.show()