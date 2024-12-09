import sympy as sp
t = sp.symbols('t') 
f_rec = sp.fourier_series(t, (t, -1, 1)).truncate(8)
f_rec
f_rec = sp.fourier_series(-abs(2*t) + 1, (t, -1, 1)).truncate(8)
f_rec
f_rec = sp.fourier_series(abs(sp.sign(t)), (t, -1, 1)).truncate(8)
f_rec
f_rec = sp.fourier_series(sp.Piecewise((sp.sign(t), t >= 0), (0, t < 0)), (t, -1, 1)).truncate(8)
f_rec