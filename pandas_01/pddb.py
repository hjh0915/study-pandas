import pandas as pd 

def get_data():
    """从csv文件获取数据"""
    
    df = pd.read_csv('./initdata/data.csv', names=[
        'tran_date', 'timestampl', 'acc', 'amt', 'dr_cr_flag', 'rpt_sum'])

    return df