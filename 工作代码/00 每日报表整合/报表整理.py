# -*- coding: utf-8 -*-

"""
Created on Thu Nov  8 10:12:11 2018

@author: liu14
"""

# %%
import pandas as pd
import os
os.chdir('D:\\code\\PYthon_Study\\工作代码\\00 每日报表整合\\数据')
# os.chdir('D:\\user\\Documents\\00code\\PYthon_Study\\工作代码\\00 每日报表整合\\数据')
data_fin = pd.DataFrame()
exl_sheet_name = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '数据表']
# %%

for filename in os.listdir(r'D:\\code\\PYthon_Study\\工作代码\\00 每日报表整合\\数据'):

data_year = pd.DataFrame()
for i in exl_sheet_name:
    data = pd.read_excel('2016年12月份日报表.xls', sheet_name = i, header=0)
    data.columns = data.columns.astype(str)
    
    del data['Unnamed: 2'], data['Unnamed: 3']
    
    data_to_pip = data[:2]
    data_to_one = data[2:20].reset_index(drop=True)
    data_to_two = data[37:57].reset_index(drop=True)
    
    data_to_one = data_to_one.drop(range(2,11))
    data_to_one = data_to_one.drop([12, 13])
    
    data_to_two = data_to_two.drop(range(4,13))
    data_to_two = data_to_two.drop([0,1,14, 15])
    
    data_to_one['日期'] = [i+j for i,j in zip((['#5']*4+['#6']*3), (data_to_one['Unnamed: 1']))]
    data_to_two['日期'] = [i+j for i,j in zip((['#7']*4+['#8']*3), (data_to_two['Unnamed: 1']))]
    data_to_pip['日期'] = [i+j for i,j in zip((['管道数据:']*2), (data_to_pip['Unnamed: 1']))]
    
    '''
    data_to_one.index = data_to_one['日期']
    data_to_two.index = data_to_two['日期']
    data_to_pip.index = data_to_pip['日期']
    '''
    
    data_mouth = pd.concat([data_to_pip,data_to_one])
    data_mouth = pd.concat([data_mouth,data_to_two])
    data_mouth.index = data_mouth['日期']
    del data_mouth['Unnamed: 1'], data_mouth['日期']
    del data_to_one, data_to_two, data_to_pip
    
    data_mouth = data_mouth.T
    data_year = pd.concat([data_year,data_mouth])

data_year = data_year.dropna(axis=0, how='all')
data_year.index.name = '日期'
data_year = data_year.reset_index()
data_year = data_year.drop_duplicates(subset='日期',keep='first')

writer = pd.ExcelWriter('year.xlsx')
data_year.to_excel(writer,'2016')
writer.save()

