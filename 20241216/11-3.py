import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def mydft2(x):
    N = len(x)
    fx = 1j*np.zeros(N)
    n = np.arange(0,N)
    for k in range(N):
        fx[k] += np.sum(x * np.exp(-1j*2*np.pi*k*n/N))
    return fx
