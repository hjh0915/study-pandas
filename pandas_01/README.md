使用pandas读取csv文件数据
======================
import pandas as pd                                                     

df = pd.read_csv('./initdata/data.csv', names=['tran_date', 'timestampl', 
 'acc', 'amt', 'dr_cr_flag', 'rpt_sum'])

names=[列名]