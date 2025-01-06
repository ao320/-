import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def mydft3(x):
    N = len(x)
    x = x.reshape(N,1)
    n = np.arange(0,N).reshape(1,N)
    k = np.arange(0,N).reshape(1,N)
    w = np.exp(-1j*2*np.pi/N)
    fx = np.dot(w**np.dot(k.T, n), x)
    return fx
