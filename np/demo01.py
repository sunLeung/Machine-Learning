import numpy as np
import math

# array = np.array([[1, 2, 3], [2, 3, 4]], dtype=np.float)  # 将列表转为矩阵
# print(array.dtype)
# print(array.ndim)
#
# a = np.linspace(1, 10, 5).reshape((5, 1))
# print(a)

# rng = np.random
#
# for i in range(10):
#     print('i=', i, 'randn=', rng.randn())

x = np.array([50, 100, 100, 60, 50])
y = np.asarray([73, 70, 75, 72, 70])

# 数学期望（均值）
print(x.mean())

# 方差=（sum(x-e)**2）/ n
x_var = ((50 - 72) ** 2 + (100 - 72) ** 2 + (100 - 72) ** 2 + (60 - 72) ** 2 + (50 - 72) ** 2) / x.shape[0]
print(x_var)
print(x.var())

# 标准差=方差开方
print(math.sqrt(x_var))
print(x.std())

print('x var:', x.var())
print('y var:', y.var())
print('x std:', x.std())
print('y std:', y.std())
