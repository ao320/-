import numpy as np
import matplotlib.pyplot as plt
K = 1
T = 1
t = np.arange(0, 5, 0.01)
y = 1 - K * np.exp(-t/T)
print('y = \n', y)
plt.plot(t,y)
plt.grid()
plt.xlabel('Time $t$ [sec]')
plt.ylabel('Output $y(t)$')
plt.show()