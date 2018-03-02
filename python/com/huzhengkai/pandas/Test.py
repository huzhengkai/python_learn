import pandas as pd
import numpy as np

a = np.arange(12).reshape(3,4)
df = pd.DataFrame(a)
print(df)

#取行数据
print(df.loc[1])
print(df.iloc[1])
#取列数据
print(df.loc[:,[0,3]])
print(df.iloc[:,[0,3]])
































