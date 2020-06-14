使用pandas创建时间序列
===================
将原有的timestampl时间 20191127105937 变为 2019-11-27 10:59:37
```
df['timestamp2'] = df['timestampl'].map(
    lambda x: datetime.strptime(str(x), '%Y%m%d%H%M%S')
)
```

创建一个新的时间序列，每间隔30分钟
```
df['interval'] = df['timestamp2'].dt.ceil('30T')
```