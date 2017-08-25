#!/usr/local/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import datetime

df = pd.DataFrame(
    {'A': pd.Categorical(['s', 's']),
     'B': np.array([1, 1], dtype='int32'),
     'C':[2,2]})
print(df)

out = df.groupby('A').sum().reset_index()
out.to_csv('demo.csv',index=False)
