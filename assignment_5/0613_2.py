"""
考虑由两个向量（X，Y）描述的路径，如何使用等距样本对其进行采样
"""
import numpy as np

phi = np.arange(0, 10 * np.pi, 0.1)
a = 1
x = a * phi * np.cos(phi)
y = a * phi * np.sin(phi)

dr = (np.diff(x) ** 2 + np.diff(y) ** 2) ** .5  # segment lengths
r = np.zeros_like(x)
r[1:] = np.cumsum(dr)  # integrate path
r_int = np.linspace(0, r.max(), 200)  # regular spaced path
x_int = np.interp(r_int, r, x)  # integrate path
y_int = np.interp(r_int, r, y)
