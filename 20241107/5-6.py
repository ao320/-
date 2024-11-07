import numpy as np
import matplotlib.pyplot as plt
nend = 64; n = np.arange(0, nend)  # Time index n：0〜63
w = np.pi / 8  # Angular Frequency ω：π/8
ejwn = np.exp(1j * w * n)
plt.subplot(2,1,1)
plt.stem(n,ejwn.real);
plt.grid()
plt.ylabel('Re[$e^{j¥omega n}$]')
plt.subplot(2,1,2)
plt.stem(n,ejwn.imag);
plt.grid()
plt.ylabel('Im[$e^{j¥omega n}$]')
plt.xlabel('Time $n$'); 
plt.show()