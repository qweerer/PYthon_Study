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
data = pd.read_excel('2016年12月份日报表.xls', sheet_name = '1月', header=0)

# %%
data_to_pip = data[:2]
data_to_one = data[2:20].reset_index(drop=True)
data_to_two = data[37:57].reset_index(drop=True)
