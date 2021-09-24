## 一：内核更换

1. 安装稳定内核版本和对应头文件

```shell
pacman -S linux-lts linux-lts-header
```

2. 卸载原先linux内核

```shell
pacman -Rsdd linux
```

3. 生成LTS版本的grub.cfg

```shell
grub-mkconfig -o /boot/grub/grub.cfg 
grub-mkconfig > /boot/grub/grub.cfg

#grub.cfg路径需改成自己实际的
```
这样在通过grub启动的时候就是用的稳定版内核了。

4. 重启

## 二：修复受影响软件

1. Vritualbox无法启动原先的虚拟机

因为版本不同，Virtualbox的版本也是不同的，对应lts内核，使用的是virtualbox-host-dkms，重装一下替换掉原来的版本即可：

```shell
pacman -S virtualbox-host-dkms
```

另外启动虚拟机还需要加载一个必须的内核模块：vboxdrv

```shell
modprobe vboxdrv
# 再重新加载一下vbox的各个相关模块：
vboxreload
```