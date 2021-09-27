# qemu
#linux/program 

## 制定密码
由于在[centos官方](http://cloud.centos.org/centos)下载的qcow2文件没有root密码, 需要先设置密码<br>
详细说明可以参考suse文档[libguestfs | Virtualization Guide | SUSE Linux Enterprise Server 12 SP4](https://documentation.suse.com/sles/12-SP4/html/SLES-all/chap-guestfs.html)
suse: `zypper in guestfs-tools`
centos: `libguestfs-tools`
```shell
virt-customize -a rhel-server-7.6.qcow2 --root-password password:StrongRootPassword
```

## qcow2镜像转换

转换`qcow2`需要用到`qemu-img`.</br>
在centos中, 直接使用"yum install qemu-img"<br>
在suse中, 安装" zypper in --no-recommends qemu-tools"

```shell
convert [--object objectdef] [--image-opts] [--target-image-opts] [--target-is-zero] [--bitmaps] [-U] [-C] [-c] [-p] [-q] [-n] [-f fmt] [-t cache] [ src_cache] [-O output_fmt] [-B backing_file] [-o options] [-l snapshot_param] [-S sparse_size] [-r rate_limit] [-m num_coroutines] [-W] [--salvage] fename [filename2 [...]] output_filename
```

例如
```shell
qemu-img convert -f qcow2 -O vdi CentOS-7-x86_64-GenericCloud-2009.qcow2c centos.vdi
```

