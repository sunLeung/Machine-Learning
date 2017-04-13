import pandas as pd

data = [[1, 2, 3], [4, 5, 6]]
index = [0, 1]
columns = ['a', 'b', 'c']
df = pd.DataFrame(data=data, index=index, columns=columns)
print(df)
print('===================================')
print(df.iloc[:,[1]])
