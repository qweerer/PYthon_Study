## 下载

在[python官网](https://www.python.org/)下载`embeddable package`

## 下载pip
下载[pip-install](https://bootstrap.pypa.io/get-pip.py)。并在cmd 中运行
```cmd
.\python get-pip.py
```

## 修改文件
修改根目录下`python[版本号]._pth`文件. 将其`#import site`取消注释
```python
import site
```

之后就可以去`Scripts`目录使用pip安装模块了

## bat命令
```bash
@echo off
chcp 65001 #切换为utf-8 编码
echo 即将开始运行
.\python-embedable\python.exe .\main\main.py

pause
```