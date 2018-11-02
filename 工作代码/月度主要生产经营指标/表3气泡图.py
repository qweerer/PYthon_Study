# -*- coding: utf-8 -*-
import os
import pandas as pd
# import time
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool
from bokeh.models import ColumnDataSource

# %%
os.chdir('D:\\user\\Documents\\00code\\PYthon_Study\\工作代码\\月度主要生产经营指标')
data03 = pd.read_excel('宝昌发电公司月度主要生产经营指标汇总表.xlsx',sheet_name=2,header=2)
data03['厂名'] = data03['厂名'].str.replace('\n','')
data03['厂名'] = data03['厂名'].str.replace('（','(')
data03['厂名'] = data03['厂名'].str.replace('）',')')
data03.index = data03['厂名']
del data03['单位'],data03['厂名'],data03['华  电 ']
data03 = data03.T
# %%

data03.columns=['1','2','3','4','5','6']
data03.index.name = 'cty'
data03['4'] = data03['4']/10

name_cty = data03.index.tolist()


p = figure(plot_width=500, plot_height=400,
           title='不同9E电厂在2018年19月的指标情况',
           tools='reset,wheel_zoom,pan,crosshair,box_select,save',
           x_range=data03.index.tolist())

source = ColumnDataSource(data=data03)

p.circle(x='cty', y='1', size='4', source=source)

show(p)










output_file("111.html")
p = figure(plot_width=1500, plot_height=400,
           title='不同9E电厂在2018年19月的指标情况',
           tools='reset,wheel_zoom,pan,crosshair,box_select,save')

p.circle(x=data03.index.tolist(), y='容量', size='计划电量(完成率)', source=data03,
          line_color='black', line_alpha=0.8, line_width=0.5, line_dash=[4, 2])

show(p)



#%%
color = ['green', 'blue', 'red']
hover = HoverTool(tooltips=[('电影均分', '@score'),
                            ('这一年电影产量', '@num')])
p = figure(plot_width=1500, plot_height=400,
           title='不同9E电厂在2018年19月的指标情况',
            tools=[hover, 'reset,wheel_zoom,pan,crosshair,box_select,save'])
i = 0

source = ColumnDataSource(data03)
p.circle(x='years', y='score', size='num', source=source,
          fill_color=color[i], fill_alpha=0.6,
          line_color='black', line_alpha=0.8, line_width=0.5, line_dash=[4, 2])
