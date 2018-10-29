# 环境变量
1. 在终端输入`$sudo nano /etc/profile`，打开profile文件
2. 在文件末尾添加一行：`export PATH=~/anaconda3/bin:$PATH`
或者
```
# 将anaconda的bin目录加入PATH
echo 'export PATH="~/anaconda3/bin:$PATH"' >> ~/.bashrc
# 更新bashrc以立即生效
source ~/.bashrc
```

*ps.也可以在终端中输入echo $PATH查看已有的环境变量，确认输出里是否已有Anaconda路径了。*

# 打开自带软件
```
终端中输入$spyder,或者anaconda-navigator
```

# vscode

把配置文件的root权限去掉就好了

cd ~/.config 
sudo rm -rf ./Code/