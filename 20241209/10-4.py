import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
<<<<<<< HEAD

=======
>>>>>>> 7763b3754bfeeb09aa6aca5c5133b2e3e01a2aaa
f = 3
fs = 20
t = np.arange(0, 2, 1/fs)
fk = np.arange(0, fs, fs/(2*fs))
sig = np.sin(2*np.pi*f*t)
fsig = np.fft.fft(sig)
print(fsig)
plt.figure()
plt.plot(t,sig)
plt.grid()
plt.figure()
plt.plot(fk, abs(fsig))
<<<<<<< HEAD
plt.grid()
=======
plt.grid()
>>>>>>> 7763b3754bfeeb09aa6aca5c5133b2e3e01a2aaa
