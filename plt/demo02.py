import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd

# 读取文件
d = pd.read_table('E:/Umeng/tmp/ucnews.csv', delimiter=',',)
val = []
for i in range(0, 1000, 1):
    min = 0
    max = 0
    for j in d['abs']:
        if j == i:
            min += 1
        else:
            max += 1
    val.append([i, min])
# print(val)
df = pd.DataFrame(data=val)
df = df.set_index(0).sort_index()
df.plot(kind='bar')
plt.show()


# d.columns = ['pv']
# # d = d.set_index('time').sort_index()
# d.plot(kind='bar')
# plt.show()
