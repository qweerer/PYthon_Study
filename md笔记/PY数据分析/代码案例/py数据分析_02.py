# %%
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# %%


def f(x, y):
    return ((x**2) - (y**3) + (6*x*(y**2)) - 12) / (5*y - 7*x*y + 3)


fig = plt.figure(0, figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
x = y = np.linspace(-5.0, 5.0, 1001)#生成x和y坐标刻度
X, Y = np.meshgrid(x, y)#生成构成（x,y）坐标点的X矩阵，Y矩阵
# %%
import numpy as np
from mpl_toolkits.mplot3d import Axes3D#调入三维图框工具
import matplotlib.pyplot as plt#调入做图库
f=lambda x,y:((x**2)-(y**3)+(6*x*(y**2))-12)/(5*y-7*x*y+3)#定义函数
fig = plt.figure(0,dpi=120,figsize=(8,8))#定义画布大小
ax = fig.add_subplot(111, projection='3d')#定义画框
x = y = np.linspace(-5.0, 5.0, 1000)#生成x和y坐标刻度
X, Y = np.meshgrid(x, y)#生成构成（x,y）坐标点的X矩阵，Y矩阵
zs = np.array([f(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])#把X,Y矩阵压缩成真正的坐标点，并代入计算出函数值
Z = zs.reshape(Y.shape)
ax.plot_surface(X, Y, Z,cmap='ocean')#绘制表面图
ax.set_xlabel('X Label')#设置坐标轴标签
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_zlim(-5,200)#设置z坐标刻度范围
plt.show()

# %%
x = (1, 2, 3)
X, Y = np.meshgrid(x, x)
print(X)
x = np.ravel(X)
print(x)

# %%
a = 'ojbk'
print(a[::-1])
# %%
data = np.arange(16).reshape(4, 4)
data[np.ix_([1,3], [3,1])]
