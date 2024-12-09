import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from scipy import signal
t=sp.symbols('t')
f_sig = sp.fourier_series(t,(t,-1, 1)).truncate(4)
N = 100
dt = np.linspace(-1, 1, N) 
p_sig = []
for k in range(N):
    p_sig.append(float(f_sig.subs(t,dt[k])))
t_sig = signal.sawtooth(np.pi * dt + np.pi)

plt.plot(dt ,t_sig)
plt.plot(dt ,p_sig)
plt.show()
