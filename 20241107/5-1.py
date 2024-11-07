import numpy as np
import matplotlib.pyplot as plt
n = np.array([-5,-4,-3,-2,-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10]) # Time
d = np.array([ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) # Unit sample
plt.stem(n,d)
plt.grid()
plt.xlabel('Time $n$')
plt.ylabel('$¥delta(n)$')
plt.show()