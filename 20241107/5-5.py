import numpy as np
import matplotlib.pyplot as plt
nend = 64; n = np.arange(0, nend)  # Time index n：0〜63
w = np.pi / 8  # Angular Frequency ω：π/8
ejwn = np.exp(1j * w * n)
plt.stem(n,ejwn.real);
plt.stem(n,ejwn.imag, linefmt="red");
plt.grid()
plt.xlabel('Time $n$'); 
plt.ylabel('$e^{j¥omega n}$')
plt.show()