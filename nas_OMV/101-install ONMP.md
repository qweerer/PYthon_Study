# Install ONMP

## mount werehouse disk with system starting

硬盘的`sd#`编号在OMV `File Systems`中查看

```shell
mount -t ext4 /dev/sd#1 /mnt/Hhd_01_120G


vi /etc/fstab # 按一下i编辑文件

# 添加下面这一行
/dev/sda1 /mnt/onmp ext4 defaults 0 1
# 按一下Esc再输入冒号`:`，输入wq回车保存
```

开机自动挂载

```Shell
vi /etc/rc.local # 编辑，vim基本用法和上面一样

# 在exit 0之前添加以下命令，开机后会自动执行挂载
mount -a
```

在仓库盘盘上创建一个空的 opt 文件夹
在系统根目录创建 opt 文件夹，并绑定U盘的 opt 文件夹

```Shell
mkdir /mnt/Hhd_01_120G/onmp/opt
mkdir /opt
mount -o bind /mnt/Hhd_01_120G/onmp/opt /opt
# 可以用 mount 或 df -h 命令查看是否挂载成功
```



## nextcloud

如果数据目录不能设定
```
chown -R nobody:nogroup /sharedfolders/disk_120G/[file]nextcloud
```