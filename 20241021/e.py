import numpy as np
import matplotlib.pyplot as plt
a = 1
b = 1
t = np.arange(0, 5, 0.01)
y = a * np.sin(b * np.cos(t)) + b * np.cos(a * np.sin(t))
print('y = \n', y)
plt.plot(t,y)
plt.grid()
plt.xlabel('Time $t$ [sec]')
plt.ylabel('Output $y(t)$')
plt.show()