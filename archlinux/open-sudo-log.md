
## 编辑 /etc/rsyslog.conf

```shell
vim /etc/rsyslog.conf
#在文件底部添加一行
local2.debug                           /var/log/sudo.log
```

## 编辑sudo

```shell
vim /etc/sudoers.d/showlog

visudo
#添加3行
Defaults logfile=/var/log/sudo.log
Defaults loglinelen=0
Defaults !syslog

touch  /var/log/sudo.log
```
