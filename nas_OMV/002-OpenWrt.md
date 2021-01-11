# OpenWrt

## overlay 与 docker 空间扩容

常用命令

```shell
lsblk # 查看分区表
mkfs.ext4 /dev/sda9 #格式化， sda#为分区编号
mount /dev/sda9 /mnt/sda9
```

1. 分区工具:cfdisk

```shell
cfdisk /dev/sda #sda为分区表中的硬盘编号
```

2. 格式化与挂在分区

```shell
mkfs.ext4 /dev/sda9 #格式化， sda#为分区编号
mount /dev/sda9 /mnt/sda9
```

3. 备份overlay文件

```shell
cp -r /overlay/* /mnt/sda9
```

`overlay`与`docker`空间的只能是一个盘

