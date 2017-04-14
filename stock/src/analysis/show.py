#!/usr/bin/python3
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

d = pd.read_table('../../data/stock_data/sz_a/sz000027', delimiter='`', header=None)
d = d.iloc[:, [4, 31, 32]]
d.columns = ['price', 'date', 'time']
d = d[d.date == '2017-04-14']
d = d.set_index('time').sort_index()
d.plot()
plt.show()

