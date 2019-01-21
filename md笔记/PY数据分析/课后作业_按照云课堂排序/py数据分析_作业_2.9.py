# -*- coding: utf-8 -*-
"""
题目:
    绘制势图:f(x,y) = xe^{-(x^2 + y^2)}
@author: liu14
"""

# %%
import numpy as np
import matplotlib.pyplot as plt


def hightNumber(x, y):
    return x * np.exp((-x**2) - (y**2))

# y = x = np.linspace(-2.0,2.0,500)


x = y = np.arange(-2, 2, 0.01)
X, Y = np.meshgrid(x, y)
Z = hightNumber(X, Y)

# fig = plt.figure(num=0, figsize=(8,8))
fig, axes1 = plt.subplots(2, 2, dpi=150, figsize=(5, 5))
axes1[0, 0].imshow(Z)
axes1[0, 1].imshow(Z, cmap=plt.cm.gray)
axes1[1, 0].imshow(Z, cmap=plt.cm.cool)
axes1[1, 1].imshow(Z, cmap=plt.cm.hot)
plt.show()
