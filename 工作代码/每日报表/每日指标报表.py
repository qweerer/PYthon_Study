# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 10:12:11 2018

@author: liu14
"""

# %%
import pandas as pd
import os
# os.chdir('D:\\code\\PYthon_Study\\工作代码\\每日报表')
os.chdir('D:\\user\\Documents\\00code\\PYthon_Study\\工作代码\\每日报表')
year = 365
# %%
data01 = pd.read_excel('每日报表基础文件.xlsx', header=0)
'''
nM = str(data01['num'][data01['name'] == '昨日日期'].tolist()[0])[:2]
nD = str(data01['num'][data01['name'] == '昨日日期'].tolist()[0])[2:]
'''
yM = str(data01['num'][data01['name'] == '昨日日期'].tolist()[0])[5:7]
yD = str(data01['num'][data01['name'] == '昨日日期'].tolist()[0])[8:10]
nM = str(data01['num'][data01['name'] == '今日日期'].tolist()[0])[5:7]
nD = str(data01['num'][data01['name'] == '今日日期'].tolist()[0])[8:10]

dayGas = data01['num'][data01['name'] == '当日燃料消耗'].tolist()[0]/10000

dayFaDian = data01['num'][data01['name'] == '日发电量'].tolist()[0]/10000
mouLeiJi = data01['num'][data01['name'] == '月累计发电量'].tolist()[0]/10000
yearLeiJi = data01['num'][data01['name'] == '年累计发电量'].tolist()[0]/10000

# %% 广东公司大唐集团月度电量完成日督导情况表
# 已经不需要此表
'''
lyFaDian = data01['num'][data01['name'] == '去年日发电量'].tolist()[0]/10000
lyLeiJi = data01['num'][data01['name'] == '去年月累计发电量'].tolist()[0]/10000

lyFaDian = dayFaDian - lyFaDian
lyLeiJi = mouLeiJi - lyLeiJi

dayok = pd.DataFrame({'当日':dayFaDian, '月累计':mouLeiJi,'去年当日差值': lyFaDian, '去年累计差值': lyLeiJi}, index = [0])

writer = pd.ExcelWriter('./输出/电量完成日out.xlsx')
dayok.to_excel(writer,'shell1')
writer.save()

del lyFaDian, lyLeiJi, dayok
'''
# %% 9E对标
'''
data02 = pd.read_excel('利用小时统计分析表2018.xlsx', header=0)
data03 = pd.read_excel('下发的利用小时对标.xlsx', header=0)
data03['num'] = data03['num']/10

nDownMou = int(str(data01['num'][data01['name'] == '对标电量时间'].tolist()[0])[:2])
nDownDay = int(str(data01['num'][data01['name'] == '对标电量时间'].tolist()[0])[2:])
LDownMou = int(str(data01['num'][data01['name'] == '上次对标电量时间'].tolist()[0])[:2])
LDownDay = int(str(data01['num'][data01['name'] == '上次对标电量时间'].tolist()[0])[2:])

days = nDownDay - LDownDay

data04 = data02[nDownMou-1:nDownMou].T
data04 = pd.merge(data04, data03, left_index=True, right_on='name').reset_index(drop=True)

data03 = data02[data02['Unnamed: 0'] == '估计容量'].T
data04 = pd.merge(data03, data04, left_index=True, right_on='name')

data04.columns = ['容量', '原数据','厂名','现数据']
data04['原数据'] = data04['原数据'].astype(float)
data04['差值'] = data04['现数据'] - data04['原数据']
data04['每日差值'] = data04['差值'] /days



data03 = data04.copy()
data03.index = data03['厂名']
del data03['厂名']
data03 = data03.T
data03 = data03.astype(float)
data03['美视A'] = data03['美视A']+data03['南天（美B）']
del data03['南天（美B）'], data03['前湾'], data03['能东']
data03 = data03.T
data03['每日利用小时'] = data03['每日差值']/data03['容量']
data03 = data03.sort_values('每日利用小时', ascending=False)
data03['每日利用小时排名'] = [x+1 for x in range(0,5)]
'''
# %%

# 判断机组运行情况
a = 0
b = 0

c = data01['num'][data01['name'] == '5,6机组是否运行'] == '是'
if c.tolist()[0]:
    a = 1
c = data01['num'][data01['name'] == '7,8机组是否运行'] == '是'
if c.tolist()[0]:
    b = 1

if a+b == 2:
    a = '5、6、7、8号机组运行'
elif a+b == 0:
    a = '5、6、7、8号机组全部停备'
else:
    if a == 1:
        a = '5、6号机组运行、7、8号机组停备'
    else:
        a = '7、8号机组运行、5、6号机组停备'

# 开始打印结果
print('{}月{}日宝昌公司{}'.format(yM, yD, a), end=';')
del a, b, c
print('日发电量{}万千瓦时;月累计发电量{}万千瓦时'.format(int(dayFaDian+0.5), int(mouLeiJi+0.5)), end=',')
# 计算完成月计划情况
lz = data01['num'][data01['name'] == '月计划力争值'].tolist()[0]
lzb = str((mouLeiJi/lz)*100+0.005)[:5]
print('完成分公司月计划（力争值{}万千瓦时）的{}%'.format(lz, lzb), end='；')
# 计算完成年下发电量情况
lz = data01['num'][data01['name'] == '年计划发电量'].tolist()[0]
lzb = (yearLeiJi/lz)*100
print('年累计发电量{}万千瓦时，完成分公司下达年发电量计划（{}万千瓦时）的{}%'.format(int(yearLeiJi+0.5), lz, str(lzb+0.005)[:5]), end=',')
# 计算高于时间进度情况
lz = data01['num'][data01['name'] == '昨天是今年第几天'].tolist()[0]
lzb = lzb - (lz/year)*100
print('高于时间进度%.2f%%'%lzb, end=',')

lz = data01['num'][data01['name'] == '年计划发电量'].tolist()[0]
print('完成年发电量计划还需%i千瓦'%(lz-yearLeiJi), end='时')
print('(约%i套开机)'%((lz-yearLeiJi)/250+0.5), end=',')

print('目前尚未执行的开机计划数为  套(今天多争取了 套开机)', end='。')

# 判断今天的运行情况
c = str(data01['num'][data01['name'] == '今日发电情况'].tolist()[0])

print('今天({}月{}日){}。(计划营销部)'.format(nM, nD, c))
print('累计%i天'%lz)
del lz, lzb, nD, nM

# %% 一般情况下的报表

dayok = pd.DataFrame({'当日':dayFaDian, '月累计':mouLeiJi,'年累计': yearLeiJi, 
                      '日利用小时': dayFaDian/36.68, '月利用小时': mouLeiJi/36.68,
                      '年利用小时': yearLeiJi/36.68, '每日气耗':dayGas}, index = [0])

dayok = dayok.T
writer = pd.ExcelWriter('./输出/电量完成日out.xlsx')
dayok.to_excel(writer,'shell1')
writer.save()

del dayok



