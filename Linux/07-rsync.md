# rsync

#linux/program 

## 简单

```shell
# 将a目录同步至b
rsync -a /tmp/a /tmp/b
# 将a目录中文件同步至b
rsync -a /tmp/a/ /tmp/b
# -v 显示日志
rsync -av /tmp/a/ /tmp/b

# 使用ssh远程同步
rsync -av -e "ssh -p 22" /tmp/a/ root@192.168.2.1:/tmp/b
```

## 后台服务

默认在`/etc/rsyncd.conf`

```conf
uid = root
gid = root
secrets file = /opt/www/00-config/rsync/rsyncd.secrets

[test]
path = /tmp/test
list = yes
read only = no
ignore errors
auth users = tom
hosts allow = 192.168.2.1/24 # 哪些电脑可以访问rsync服务   
hosts deny = 0.0.0.0/0 # 哪些电脑不可以访问rsync服务
```

设置密码文件，`chmod 600 /opt/www/00-config/rsync/rsyncd.secrets`

```test
tom:0000
```
也可与指定config
`rsync --daemon --config "/opt/www/00-config/rsync/rsyncd.conf"`


## 客户端操作

```shell
# 查看服务器所有服务
rsync 127.0.0.1::

# 查看test模组下文件
rsync 127.0.0.1::test

# 同步目录
rsync -av 127.0.0.1::test/ /tmp/a

# 使用密码
rsync -av --password-file=/opt/www/00-config/rsync/password tom@127.0.0.1::test/ /tmp/a

# 设置密码文件
echo "0000" > /opt/www/00-config/rsync/password
chmod 600 /opt/www/00-config/rsync/password

```

