import numpy as np
import matplotlib.pyplot as plt
nend = 64; n = np.arange(0, nend)  # Time index n：0〜63
w = np.pi / 8  # Angular Frequency ω：π/8
ejwn = np.exp(1j * w * n)
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax1.stem(n, ejwn.real)
ax1.grid()
ax1.set_label('Re[$e^{j¥omega n}$]')
ax2 = fig.add_subplot(2,1,2)
ax2.stem(n,ejwn.imag);
ax2.grid()
ax2.set_ylabel('Im[$e^{j¥omega n}$]')
ax2.set_xlabel('Time $n$')
plt.show()