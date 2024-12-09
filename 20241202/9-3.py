import sympy as sp
t = sp.symbols('t') 
f_rec = sp.fourier_series(sp.sign(t), (t, -1, 1)).truncate(8)
f_rec
