import numpy as np
import matplotlib.pyplot as plt
f = 5
t = np.arange(0, 1, 0.001)
x = np.sin(2 * np.pi * f * t)
plt.plot(t,x)
plt.grid()
plt.xlabel('Time [sec]')
plt.show()
