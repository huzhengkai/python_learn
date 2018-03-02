import pandas as pd
import numpy as np

a = np.arange(12).reshape(3,4)
df = pd.DataFrame(a)

df.index = ['a','b','c']
print(df)

#报错： cannot do label indexing on <class 'pandas.core.indexes.base.Index'> with these indexers [1] of <class 'int'>
#print(df.loc[1])
print(df.iloc[1])

print(df.loc['b'])
#报错：cannot do positional indexing on <class 'pandas.core.indexes.base.Index'> with these indexers [a] of <class 'str'>
#print(df.iloc['a'])

print(df.ix[0])
print(df.ix['a'])







