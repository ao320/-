import numpy as np
import matplotlib.pyplot as plt
alpha = 10.0
n = np.array([-5,-4,-3,-2,-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10]) # Time
u = np.array([ 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) # Unit step
a = alpha ** n * u
plt.stem(n,a)
plt.grid()
plt.xlabel('Time $n$')
plt.ylabel('$¥delta(n)$')
plt.show()