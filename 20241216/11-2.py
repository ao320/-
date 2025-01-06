import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def mydft1(x):
    N = len(x)
    fx = 1j*np.zeros(N)
    for k in range(N):
        for n in range(N):
            fx[k] += x[n] * np.exp(-1j*2*np.pi*k*n/N)
    return fx

