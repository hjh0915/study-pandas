使用pandas创建一个自定义时间序列
============================

根据起始时间和终止时间创建一个以30分钟为间隔的时间序列
---------------------------------------------
```
import pandas as pd 
import numpy as np

rng = pd.date_range(start, end, freq='30T') 
ts = pd.Series(rng, index=np.arange(len(rng)))  
ts = pd.DataFrame(ts, columns=['time'])  
```
*freq为时间频率*
*DatetimeIndex->Series->DataFrame*

组合两个时间列，若存在数据为0，则对应时间的数据填写为0
---------------------------------------------
```
df2 = pd.merge(ts, tm, left_on=['time'], right_on=['interval'], how='left') 
df2 = df2[['time', 'amt']].fillna(0)
```