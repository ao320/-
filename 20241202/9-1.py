#モジュールのインポート
import matplotlib.pyplot as plt 
import numpy as np
P= 2#周期
maxk =7#次数
N = 100 #点数
dt = np.linspace(-1, 1, N)#時間軸
sig = np.sign(dt)#信号
sumofsin = np.zeros(N)#重ね合わせ結果を入れる配列
for k in range(1,maxk+1,2):
    sumofsin += 4*np.sin(2*np.pi*k*dt/P)/(k*np.pi) # Ehbt
plt.plot(dt,sig) # 信号を描画
plt.plot(dt, sumofsin)#重ね合わせたて得た波形を描画
plt.show()