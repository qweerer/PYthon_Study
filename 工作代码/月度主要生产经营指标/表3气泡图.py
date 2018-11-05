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
data03['利用小时'] = data03['实际发电量']/data03['容量']
data03 = data03.sort_values('利用小时',ascending=False)
data03['利用小时排名'] = [n+1 for n in range(len(data03))]
# %%
output_file("./输出/9E对标.html")

data03Pic = data03.copy()
data03Pic.columns=['1','2','3','4','5','6']
data03Pic.index.name = 'cty'
data03Pic['1'] = data03Pic['1']*1.3

color = ['#EDD1CB', '#e0b1b4', '#cf91a3', '#b77495']
         # , '#49838a', '#3e5f7e','#383c65', '#2b1e3e']
data03Pic['7'] = color

name_cty = data03Pic.index.tolist()

hover = HoverTool(tooltips=[('容量', '@1'),
                            ('经信委下达电量', '@2'),
                            ('实际发电量', '@3'),
                            ('下达电量完成率', '@4'),
                            ('利用小时', '@5')])

source = ColumnDataSource(data=data03Pic)

p = figure(plot_width=1000, plot_height=900,
           title='不同9E电厂在2018年10月的指标情况',
           tools=[hover, 'reset,ywheel_zoom,xwheel_zoom,pan,crosshair,box_select,save'],
           x_range=name_cty)

p.circle(x='cty', y='5', size='1', source=source,
         color = '7', alpha=0.9,
         line_color='black', line_width=2, line_dash=[4, 2])

p.yaxis.axis_label = "利用小时"

p.xaxis.major_label_text_font_size = '16pt'
p.xaxis.major_label_text_font_size = '14pt'

p.xgrid.grid_line_color = None
p.ygrid.grid_line_alpha = 0.9


show(p)


# %%
