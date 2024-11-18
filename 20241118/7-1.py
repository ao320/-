import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

n = np.arange(0, 9, 1)
x = np.sin(3 * n * np.pi / 5)
plt.stem(n,x,linefmt="red")
plt.grid()
plt.xlabel('n')
plt.show()