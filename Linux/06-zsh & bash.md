# ZSH

#linux #linux/program/shell

```shell
torch ~/myconfig/.zshrc
ln -sf ~/myconfig/.zshrc ~/.zshrc
```

# bash

```SHELL
vi /etc/.bashrc

#=======[.bashrc]=======#
exitstatus() {
    if [ "$?" = 0 ]
    then
        printf '\033[1;32m √ \033[0m'
    else
        printf '\033[1;31m × \033[0m'
    fi
}
# export PS1='[\u@\h \A] \[\033[1;36m\] [\$]\[\033[0m\] [] \w \n\[\033[0;33m\]In[\#]:= \[\033[0m\]'
# export PS1='[\u@MSYS \A] \[\033[1;31m\] [\$]\[\033[0m\] [] \w \n\[\033[0;33m\]In[\#]:= \[\033[0m\]'
export PS0='\n#==========[out]==========#    \n'
export PS1='\n    \n[\033[1;35m\u@MSYS\e[0m \A] \033[1;32m[\$]\e[0m [`exitstatus`] \033[1;93m\w\e[0m  \n\[\033[0;33m\]In[\#]:= \[\033[0m\]'
export PS2='In[=]:>'

export PATH=$PATH:/c/Develop/nodejs
```


## shell中颜色

| 高亮 | 下划线 | 闪烁 |
| ---- | ------ | ---- |
| 1    | 4      | 5    | 


| 颜色   | 黑  | 红  | 绿  | 黄  | 蓝  | 红  | 青  | 白  |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| 前景色 | 30  | 31  | 32  | 33  | 34  | 35  | 36  | 37  |
| 背景色 | 40  | 41  | 32  | 43  | 44  | 45  | 46  | 47  | 

# shell计算器：bc
小数点
```bc
scale=2
2/3
.66
scale=8
2/3
.66666666
```

数字转换
```bc
ibase = 2
101
5

ibase = 10
obase = 2
5
101
```
```shell
bc <<< ibase=2; 101
```