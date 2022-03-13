# 自定义存储

```bash
mount /dev/nvme0n1p1 /mnt/nvme01-1t/
## 查看uuid
lsblk -fs
## 固定
vim /etc/fstab

<file system>                              <mount point>   <type> <options> <dump> <pass>
UUID=03179efe-50f1-42c0-9e11-9c557d8078df  /mnt/nvme01-1t/ ext4 defaults 0 0
03179efe-50f1-42c0-9e11-9c557d8078df 
```

在==数据中心(最上层)== >> 存储 >> 添加

## LVM

```bash
# 物理卷
## 创建
pvcreate /dev/sdc3
## 查看
pvdisplay
pvs
pvscan

# 卷组vg
##创建
vgcreate -s 4m pve /dev/sdc3 /dev/sda
## 查看
vgdisplay
vgs
vgextend pve /dev/sdb

# 分区lv
lvcreate -L 5G -n 卷名 pve
lvdisplay # 查看卷
lvs       # 查看卷
lvremove /dev/pve/data  ## 删除
lvextend -L +21.5g /dev/pve/root ## 扩容
lvextend -L 30g /dev/pve/root ## 扩容

# 同步容量
resize2fs /dev/pve/root #ext4系统
xfs_growfs /dev/pve/root #xfs

# LV缩小
umount /dev/pve/root
resize2fs /dev/pve/root 4G
e2fsck -f /dev/pve/root
resize2fs /dev/pve/root 4G
lvreduce /dev/pve/root -L 4G
```

## system-storage-manager

```bash
ssm list dev
ssm create -s lv大小 -n lv名 -fstype xfs -p 卷组名 /dev/sdb[3-5] /mnt/sdb3 #一次变完, 遵守正则表打
```