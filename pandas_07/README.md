pandas计算方差判断差异性
=====================
```
rating_std_by_title = data.groupby('title')['rating'].std()
```