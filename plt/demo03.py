import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
#读取文件
d = pd.read_table('E:/Umeng/mp/data/ucnews.csv.tar/ucnews.csv/home/ucun/orkspace/liangyx/result/ucnews.csv', delimiter='\t')
val = []
for i in range(0,5000,2):
    print(i)
# print(val)
# df = pd.DataFrame(data=val)
# df = df.set_index(0).sort_index()
# df.plot()
# plt.show()


# d.columns = ['pv']
# # d = d.set_index('time').sort_index()
# d.plot(kind='bar')
# plt.show()
