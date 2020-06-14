import pandas as pd 
from datetime import datetime, timedelta

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