# virt-customize使用示例

我们将介绍一些如何使用virt-customize自定义Qcow2和Raw OS图像格式的示例。
首先，访问集LIBGUESTFS_BACKEND：
`export LIBGUESTFS_BACKEND=direct`

## 1.设置root密码

要设置root密码，请使用以下命令：
```
# virt-customize -a rhel-server-7.6.qcow2 --root-password password:StrongRootPassword

[   0.0] Examining the guest ...
[   1.9] Setting a random seed
[   1.9] Setting passwords
[   6.8] Finishing off
```
注：
rhel-server-7.6.qcow2是要修改图像的名称。
StrongRootPassword是为root用户设置的密码。

## 2.注册RHEL系统

要注册RHEL映像并订阅可用池，请使用以下命令：
```shell
$ virt-customize -a overcloud-full.qcow2 --run-command 'subscription-manager register --username=[username] --password=[password]'
[   0.0] Examining the guest ...
[   2.0] Setting a random seed
[   2.0] Running: subscription-manager register --username=user1 --password=mypassword
[  38.5] Finishing off
$ virt-customize -a rhel-server-7.6.qcow2 --run-command 'subscription-manager attach --pool [subscription-pool]'
```

注：
[username]-替换为有效的用户名，例如–username=admin。<br>
[password]-替换为提供的用户名的有效密码。<br>
-run-command选项用于执行虚拟映像文件中的任何命令。<br>

## 3.在图像中安装软件包

可以使用以下命令在qcow2或原始磁盘映像中安装软件包：
```shell
$ virt-customize -a rhel-server-7.6.qcow2 --install [vim,bash-completion,wget,curl,telnet,unzip]

[   0.0] Examining the guest ...
[   2.1] Setting a random seed
[   2.1] Installing packages: [vim bash-completion wget curl telnet unzip]
[ 563.2] Finishing off

$ virt-customize -a rhel-server-7.6.qcow2 --install net-tools
```

## 4.上传文件

见下面的例子：
```shell
$ virt-customize -a rhel-server-7.6.qcow2 --upload rhsm.conf:/etc/rhsm/rhsm.conf

[   0.0] Examining the guest ...
[   2.9] Setting a random seed
[   3.0] Setting the machine ID in /etc/machine-id
[   3.0] Uploading: rhsm.conf to /etc/rhsm/rhsm.conf
[   3.4] Finishing off

virt-customize -a rhel-server-7.6.qcow2 --upload yum.conf:/etc/yum.conf

[   0.0] Examining the guest ...
[   1.9] Setting a random seed
[   1.9] Uploading: yum.conf to /etc/yum.conf
[   2.2] Finishing off

virt-customize -a rhel-server-7.6.qcow2 --upload proxy.sh:/etc/profile.d/

[   0.0] Examining the guest ...
[   1.9] Setting a random seed
[   1.9] Uploading: proxy.sh to /etc/profile.d/
[   2.3] Finishing off
```
格式为：`local_file_path:image_file_path`

## 5.设置时区

你还可以在OS映像文件上设置时区（[在Ubuntu 18.04终端中修改时区的方法](https://ywnz.com/linuxjc/3174.html)），比如：

```shell
virt-customize -a rhel-server-7.6.qcow2 --timezone "Asia/Shanghai"
```

## 6.上传SSH公钥

上传用户的SSH公钥：
```
$ virt-customize -a rhel-server-7.6.qcow2  --ssh-inject jmutai:file:./id_rsa.pub

[   0.0] Examining the guest ...
[   1.9] Setting a random seed
[   2.0] SSH key inject: jmutai
[   3.2] Finishing off
```

## 7.Relabel SELinux

要重新标记SELinux文件上下文，请使用：
```shell
$ virt-customize -a rhel-server-7.6.qcow2 --selinux-relabel

[   0.0] Examining the guest ...
[   2.0] Setting a random seed
[   2.0] SELinux relabelling
[   8.6] Finishing off
```

有关更多命令用法选项，请检查：
`man virt-customize`或者
`virt-customize --help`