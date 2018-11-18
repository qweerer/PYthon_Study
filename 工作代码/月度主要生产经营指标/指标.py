# -*- coding: utf-8 -*-
import os
import pandas as pd
# import time

# %% 导入数据
os.chdir('D:\\user\\Documents\\00code\\PYthon_Study\\工作代码\\月度主要生产经营指标')

data01 = pd.read_excel('宝昌发电公司月度主要生产经营指标汇总表.xlsx', sheet_name=0, header=3)
data02 = pd.read_excel('宝昌发电公司月度主要生产经营指标汇总表.xlsx', sheet_name=1, header=2)
data03 = pd.read_excel('宝昌发电公司月度主要生产经营指标汇总表.xlsx', sheet_name=2, header=2)
# 这个是标准模板
data1FaDian = pd.read_excel('发电量.xlsx')
data1FaDian.loc[1] = [n for n in range(19)]  # 初始化需要
data1FaDian['时间'].iloc[-1] = 201809

del data01['序号'], data02['序号']
data01 = data01[:-1]  # 删除字段

# %%设定当前年月时间
timP = int(input('请输入统计数据年月,格式为:(201803):'))
# timN = int(time.strftime('%Y%m',time.localtime()))
timB = data1FaDian['时间'].iloc[-1]

if timB + 1 != timP:
    print('输入值不正确,上一个月是:', timB)
    'a' - 'b'

del timB
# %% 
timP = 201810
indexNow = data1FaDian.index.tolist()[-1] + 1
data1FaDian.loc[indexNow] = [0 for n in range(19)]
data1FaDian['时间'].iloc[-1] = timP

del indexNow, timP
# %% 将提交的值转为标准化模板(电量)
colC = data1FaDian.columns.tolist()

data1FaDian['实际发电量'].iloc[-1] = data01['实际发电量'][data01['指标名称'] == '发电量(公司)']
data1FaDian['上网电量'].iloc[-1] = data01['上网电量'][data01['指标名称'] == '发电量(公司)']
data1FaDian['年累计发电量'].iloc[-1] = data02['累计完成值'][data02['指标名称'] == '发电量(公司)']
data1FaDian['年累计上网电量'].iloc[-1] = data02['累计完成值'][data02['指标名称'] == '经信委下达电量']
# # # # #
data1FaDian['分公司_月计划确保值'].iloc[-1] = data01['月计划确保值'][data01['指标名称'] == '发电量(分公司)']
data1FaDian['分公司_月计划力争值'].iloc[-1] = data01['月计划力争值'][data01['指标名称'] == '发电量(分公司)']
data1FaDian['公司_月计划确保值'].iloc[-1] = data01['月计划确保值'][data01['指标名称'] == '发电量(公司)']
data1FaDian['公司_月计划力争值'].iloc[-1] = data01['月计划力争值'][data01['指标名称'] == '发电量(公司)']

data1FaDian['分公司_年计划'].iloc[-1] = data02['年计划'][data02['指标名称'] == '发电量(分公司)']
data1FaDian['公司_年计划'].iloc[-1] = data02['年计划'][data02['指标名称'] == '发电量(公司)']
data1FaDian['经信委_年下达计划'].iloc[-1] = data02['年计划'][data02['指标名称'] == '经信委下达电量']
# # # # #
data1FaDian['分公司_本月确保值完成率'].iloc[-1] = data01['发电量/确保值'][data01['指标名称'] == '发电量(分公司)']
data1FaDian['分公司_本月力争值完成率'].iloc[-1] = data01['发电量/力争值'][data01['指标名称'] == '发电量(分公司)']
data1FaDian['公司_本月确保值完成率'].iloc[-1] = data01['发电量/确保值'][data01['指标名称'] == '发电量(公司)']
data1FaDian['公司_本月力争值完成率'].iloc[-1] = data01['发电量/力争值'][data01['指标名称'] == '发电量(公司)']

data1FaDian['分公司_年计划完成率'].iloc[-1] = data02['完成率'][data02['指标名称'] == '发电量(分公司)']
data1FaDian['公司_年计划完成率'].iloc[-1] = data02['完成率'][data02['指标名称'] == '发电量(公司)']
data1FaDian['经信委_年计划完成率'].iloc[-1] = data02['完成率'][data02['指标名称'] == '经信委下达电量']

# %%
