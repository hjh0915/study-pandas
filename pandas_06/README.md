使用pandas排序功能
================
降序排序
------
```
data.sort_values(ascending=False, by=['F'])
```

差值排序
------
```
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_values(by='diff')
```