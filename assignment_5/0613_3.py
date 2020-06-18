"""
考虑一个任意数组，编写一个函数来提取具有固定形状并以给定元素为中心的子部分
（必要时填充为“ fill”值）
"""
import numpy as np

X = np.random.randn(100)  # random 1D array
N = 1000  # number of bootstrap samples
idx = np.random.randint(0, X.size, (N, X.size))
means = X[idx].mean(axis=1)
c = np.percentile(means, [2.5, 97.5])
print(c)
