# -*- coding: utf-8 -*-

"""
Created on Thu Nov  8 10:12:11 2018

@author: liu14
"""

# %%
import pandas as pd
import os
os.chdir('D:\\code\\PYthon_Study\\工作代码\\00 每日报表整合')
# os.chdir('D:\\user\\Documents\\00code\\PYthon_Study\\工作代码\\00 每日报表整合')
# %%

data = pd.read_excel('2016年12月份日报表.xls', sheet_name = '1月', header=0)
data.columns = data.columns.astype(str)
# del data['Unnamed: 1'], 
del data['Unnamed: 2'], data['Unnamed: 3']

# %%
data_to_pip = data[:2]
data_to_one = data[2:20].reset_index(drop=True)
data_to_two = data[37:57].reset_index(drop=True)

data_to_one = data_to_one.drop(range(2,11))
data_to_one = data_to_one.drop([12, 13])

data_to_two = data_to_two.drop(range(4,13))
data_to_two = data_to_two.drop([0,1,14, 15])

