import pandas as pd 
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List 
from decimal import Decimal

def get_data():
    """从csv文件获取数据"""
    
    df = pd.read_csv('./initdata/data.csv', names=[
        'tran_date', 'timestampl', 'acc', 'amt', 'dr_cr_flag', 'rpt_sum'])

    return df

def get_time_series():
    """获取df中的时间"""
    
    df = get_data()
    # 添加一列时间
    df['timestamp2'] = df['timestampl'].map(
        lambda x: datetime.strptime(str(x), '%Y%m%d%H%M%S')
    )
    # 添加一列每隔半个小时的时间
    df['interval'] = df['timestamp2'].dt.ceil('30T')

    return df

def get_time_range_dtl(tran_date: str, dr_cr_flag: str) -> List[Dict]:
        '''时间间隔区间交易金额汇总'''
        
        df = get_time_series()

        x = datetime.strptime(tran_date, '%Y%m%d')
        d = x - timedelta(days=1)
        start = d.strftime('%Y-%m-%d') + ' 23:00:00'
        end = x.strftime('%Y-%m-%d') + ' 22:30:00'

        # 创建新的时间序列
        rng = pd.date_range(start, end, freq='30T') # freq为时间频率
        ts = pd.Series(rng, index=np.arange(len(rng)))  # DatetimeIndex->Series
        ts = pd.DataFrame(ts, columns=['time'])   # Series->DataFrame

        # 获取数据中的时间列
        tm = df[(df['tran_date']==x.strftime('%Y-%m-%d')) & (df['dr_cr_flag']==int(dr_cr_flag))][['amt', 'interval']].groupby('interval').sum()   
        tm = tm.reset_index()  # 重构索引列
 
        # 组合两个时间列，若存在数据为0，则对应时间的数据填写为0
        df2 = pd.merge(ts, tm, left_on=['time'], right_on=['interval'], how='left') 
        df2 = df2[['time', 'amt']].fillna(0)

        results = []
        for i, r in df2.iterrows():
            d = dict()
            d['time'] = r[0].to_pydatetime()
            d['amt'] = Decimal(str(round(r[1], 2)))
            results.append(d)
        
        return results  