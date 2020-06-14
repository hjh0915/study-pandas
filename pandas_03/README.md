pandas基础
=========
import pandas as pd 

Series
-----------
x = pd.Series([1,4,2,9,190])
x输出的是索引一列，数值一列
此时x为int64类型

x = pd.Series(['a', 9, 1, 'b']) 
此时x为object类型

*若想要自定义索引列可以添加index*
pd.Series(['a', 9, 1, 'b'], index=['one','two', 'three','four']) 

DataFrame
---------
添加数据（及对应的列名）
pd.DataFrame(data, columns=[''])

索引对象
-------
import numpy as np

x = pd.Index(np.arange(3))   
Out: Int64Index([0, 1, 2], dtype='int64')
