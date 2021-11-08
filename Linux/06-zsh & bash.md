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