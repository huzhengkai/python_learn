import pandas as pd
import numpy as np


data = [['bar','one','z',1.0],
        ['bar','two','y',2.0],
        ['foo','one','x',3.0],
        ['foo','two','w',4.0]]
index = [0,1,2,3]
columns = ['a','b','c','d']
df = pd.DataFrame(data=data,index=index,columns=columns)
print(df)

#显然用作索引的列，值必须是唯一的
df1 = df.set_index('c')
print(df1)
df2 = df.set_index('c',drop=False)
print(df2)
#reset_index可以还原索引，重新变为默认的整型索引
df3 = df1.reset_index()
print(df3)





















