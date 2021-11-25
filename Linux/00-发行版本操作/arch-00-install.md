## 设置字体

#linux #linux/install 

```shell
setfont /user/share/kbd/consolefonts/LatGrkCyr-12x12
```

## 配置网络

```shell
# 查看网络连接
ip link
# 开启网络
ip link set enp03 up
# 扫描wifi
iwlist enp03 scan | grep ESSID
# 沈城wifi配置
wpa_passphrase China-net password > wifi.conf
wpa_supplicant -c wifi.conf -i enp03 &
# 配置dhcp
dhcpcd &
```

### 配置网络方式2

```shell
# 进入iwd网络
iwctl
device list
station wlan0 scan
# 获取扫描的网络列表
station wlan0 get-networks
station wlan0 connect wifi名
exit
```

## 设置时间

```shell
timedatectl -a
timedatectl set-ntp true
```

## ssh

执行`passwd`为安装环境设置密码，输入密码时不会有任何指示。

启动 SSH 服务：`systemctl start sshd`

执行`ip -brief address`查看 IP 地址，输出第三列是网卡对应的 IP 地址

## 分区

```shell
# 查看硬盘
fdisk -l
df -h
cfdisk
```

### 格式化分区

```shell
mkfs.fat -F32 /dev/sda1  #如果你的机器是UEFI启动模式，使用此命令初始化EFI系统分区
mkswap /dev/sda2
swapon /dev/sda2

mkfs.ext4 /dev/sda3
mkfs.ext4 /dev/sda4
```

### 挂载分区

```shell
mount /dev/sda3 /mnt

mkdir /mnt/boot
mount /dev/sda1 /mnt/boot

mkdir /mnt/home
mount /dev/sda4 /mnt/home
```

## pacman

### 镜像源系统

```shell
vim /etc/pacman.conf
# 删除Color前的#号
vim /etc/pacman.d/mirrorlist
```

或者

```shell
 #使用reflector来获取速度最快的5个镜像，并保存至/etc/pacman.d/mirrorlist
reflector -c China -a 5 --sort rate --save /etc/pacman.d/mirrorlist
```

#### 如果无法安装可以试下更新缓存

```shell
sudo pacman -Syy
```


## 安装

```shell
# pacman-key --refresh-keys
pacstrap /mnt base base-devel linux linux-firmware linux-headers vim intel-ucode/amd-ucode iwd 
```

```shell
# 保存mnt下的挂载分区
genfstab -U -p /mnt >> /mnt/etc/fstab
```

### 进入新安装的archlinux

```shell
    arch-chroot /mnt
```

```shell
ln -s /usr/bin/vim /usr/bin/vi
```

```shell
# 创建时区
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
hwclock --systohc #生成/etc/adjtime文件
```

### 设置locale

```shell
vim /etc/locale.gen
```

/#en_US 回车 找到UTF-8那一行 删掉前面的#（取消注释）
/#zh_CN 回车 找到UTF-8那一行 删掉前面的#（取消注释）

```shell
locale-gen
```

```shell
vim /etc/locale.conf
# 编辑 LANG=en_US.UTF-8
```

### 配置网络

创建并写入hostname

```shell
nano /etc/hostname
```

配置/etc/hosts文件

```shell
nano /etc/hosts
```

```host
127.0.0.1  localhost
::1  localhost
127.0.1.1  liu-arch.localdomain  liu-arch
```

### 设置root密码

```shall
passwd
```

### 安装及配置引导程序

```shell
pacman -S grub efibootmgr intel-ucode os-prober
mkdir /boot/grub
grub-mkconfig > /boot/grub/grub.cfg
```

安装grub

```shell
# 查看架构
uname - m
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=Arch Linux
```

#### 或者安装refind

```shell
mount -t efivarfs efivarfs /sys/firmware/efi.efivars/
pacman -S refind
refind-install --alldrivers
## 获取uuid
blkid
blkid -s PARTUUID -0 /value /dev/sda3
systemctl enable fstrim.time
# boot目录下的`refind_linux.conf`是内核参数,当refind找到/boot目录中的内核后会使用同文件夹下的配置文件中的参数
# 该文件在`refind-install`时一般会自动生成,需要查看,或者增加自己需要的内核参数
vim /boot/refind_linux.conf
```

```conf
"Boot using default options"     "root=PARTUUID=_XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX_ rw add_efi_memmap initrd=boot\intel-ucode.img initrd=boot\amd-ucode.img initrd=boot\initramfs-%v.img"
"Boot using fallback initramfs"  "root=PARTUUID=_XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX_ rw add_efi_memmap initrd=boot\intel-ucode.img initrd=boot\amd-ucode.img initrd=boot\initramfs-%v-fallback.img"
"Boot to terminal"               "root=PARTUUID=_XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX_ rw add_efi_memmap initrd=boot\intel-ucode.img initrd=boot\amd-ucode.img initrd=boot\initramfs-%v.img systemd.unit=multi-user.target"
```

如果refind找不到或者想要更多自定义配置,就需要到`/boot/efi/EFI/refind/refind.conf`中自行配置

```
# 配置文件中`volume`需要自己设置标签
e2label /dev/sda2 opensuse
lsblk -f
blkid
```

```conf
menuentry "Arch Linux" {
    icon     /EFI/refind/themes/refind-ambience/icons/os_arch.png
    volume   "Arch Linux"
    loader   /vmlinuz-linux
    initrd   /amd-ucode.img
    initrd   /initramfs-linux.img
    options  "root=PARTUUID=7ce1b087-1f97-4a98-ac50-408353207b92 rw"
    submenuentry "Boot using fallback initramfs" {
        initrd /initramfs-linux-fallback.img
    }
    submenuentry "Boot to terminal" {
        add_options "systemd.unit=multi-user.target"
    }
    #disabled
}
menuentry Opensuse {
    icon     /EFI/refind/icons/os_suse.png
    volume   "opensuse"
    loader   /boot/vmlinuz
    initrd   /boot/initrd
    options  "root=UUID=1a334fe5-bd00-4836-8e4b-3c4efc2ed15d splash=silent systemd.show_status=yes mitigations=auto quiet intel_iommu=on iommu=pt nvidia-drm.modeset=1 amdgpu.dpm=0 amdgpu.noretry=0"
    submenuentry "Boot to single-user mode" {
        add_options "single"
    }
    submenuentry "Boot with minimal options" {
        options "ro root=UUID=1a334fe5-bd00-4836-8e4b-3c4efc2ed15d"
    }
}
```


### 另一些可安装的包
```shell
pacman -S dhcpcd  wpa_supplicant openssh net-tools wget networkmanager network-manager-applet dialog wpa-applicant
pacman -S mtools bluez bluz-utils cups xdg-utils xdg-user-dirs alsa-utils pulseaudio pulseaudio-bluetooth reflector
```

```shell
networkmanager network-manager-applet dialog wireless_tools wpa_supplicant  mtools dosfstools ntfs-3g base-devel linux-headers reflector git
```

- bash//最基本的Bash Shell（必须）
- bzip2//提供bzip2压缩与解压缩功能（非必须，但就算不选它，系统也会自动将其装上）
- coreutils//提供GNU环境下最基本的工具与命令（必须）
- dnsutils//DNS工具（必须）
- file//文件类型识别工具（必须）
- filesystem//提供基本的文件系统结构（必须）
- findutils//用于查找相关文件（非必须）
- gawk//GNU 版本的awk，查找数据库信息的实用小程序（非必须，但就算不选它，系统也会自动将其装上）
- grep//基于正则表达式的，强大的字符串搜索工具（非必须，但就算不选它，系统也会自动将其装上）
- grub//功能强大的引导工具（必须）
- gzip//GNU 压缩工具（非必须，但就算不选它，系统也会自动将其装上）
- initscripts//系统初始化脚本，提供以下文件：（必须）
- iptables//IP过滤工具，其实就是防火墙。（非必须）
- iputils//IP配置工具，提供了ping与tftpd以及traceroute等，网络常用命令。（非必须）
- less//用于查看文本文件（可以翻页）（非必须）
- linux//Linux内核及模块（必须）
- logrotate//系统日志记录工具（非必须）
- mkinitcpio//（必须）
- mlocate//用于快速查找系统内的文件（使用locate命令前需要先用updatedb命令更新相关数据库）（非必须）
- nano或者vi//简单易用的编辑器（非必须）
- ncurses//在终端中提供类似GUI的界面，提供了清屏命令clear等东西（非必须）
- net-tools//Linux网络配置工具，提供netstat/arp/ifconfig等命令（非必须，但迟早会用到，所以还是安上算了）
- openssh//SSH连接工具（非必须，但就算不选它，系统也会自动将其装上）
- pacman（pacman-key命令由更新之后的pacman包提供）//Arch Linux的默认包管理工具（必须）
- pacman-mirrorlist//Arch Linux镜像列表（必须）
- procps（更新之后的包名叫procps-ng）//系统、进程监控工具（必须）
- reiserfsprogs//Reiserfs 文件系统工具（必须）
- sed//GNU stream editor（也就是文本流编辑工具，妙的是，这个工具没有界面，只使用参数）（非必须）
- syslog-ng//带高级网络和过滤功能的下一代syslogd（必须）
- sysvinit//Linux System V Init，提供/init/poweroff/reboot/shutdown等东东，这个当然是必须品 （必须）
- tar//压缩与打包的工具（非必须，但就算不选它，系统也会自动将其装上）
- wget//Shell下的下载工具（非必须）
- which//显示命令的全路径的工具（非必须）
- xz //使用 LZMA压缩算法的无损数据压缩文件格式。和gzip与bzip2一样（非必须，但就算不选它，系统也会自动将其装上）

#### 无线网卡驱动

`Broadcom BCM43142` 必须要在安装完Arch Linux后再安装额外的驱动，否则重启后无法连接无线网

```ssh
lspci -vnn | grep 14e4  #或者lspci -k | grep -A 2 -i network查看网卡
pacman -S broadcom-wl-dkms 
#安装驱动，如果查日志发现有No kernel 4.5.4-1-ARCH headers. You must install them to use DKMS!错误，你有可能是没有安装头文件，使用pacman -S linux-headers安装好头文件后再安装一次，大概就好了
systemctl srart NetworkManager 
systemctl enable NetworkManager  #启动网络服务
```

## 推出，重启

```shell
exit  #输入exit或按Ctrl+d退出chroot环境
umount -R /mnt  #用umount -R /mnt手动卸载被挂载的分区
reboot  #执行reboot重启系统
```

# 安装配置

```shell
pacman -Syyu
# 安装man（help)
pacman -S man
pacman -S base-devel
```

## 开机启动

```shell
systemctl enable dhcpcd
```

## 添加用户

```shell
useradd -m -G wheel qweerer
passwd qweerer
vim /etc/sudoers
# 去掉%wheel ALL
```

## 设置root可以通过ssh登录

```shell
vim /etc/ssh/sshd.config
# PermitRootLogin yes
```

## 安装另一个程序管理软件yay

```shell
wget https://aur.archlinux.org/yay.git
cd yay
makepkg -si

yay -S goole-chrome
```

## 电池管理

```shell
sudo /usr/bin/tlp start
sudo systemctl enable tlp.service 
sudo systemctl enable tlp-sleep.service
# 禁止冲突的服务
systemctl disable systemd-rfkill.service
systemctl disable systemd-rfkill.socket

# 编辑配置文件
/etc/default/tlp
```

注意： 如果存在 `NetworkManager.service`，`tlp.service` 将启动它 `NetworkManager.service`。如果您使用其它的网络管理器，请编辑 `tlp.service` 来去除此服务 (`lineWants`)或屏蔽它。

## 安装驱动

### 安装virtualbox驱动

```shell
pacman -S xf86-video-vesa
pacman -S xf86-video-vmware
pacman -S virtualbox-guest-utils
pacman -S virtualbox-guest-dkms
sudo pacman -S linux-headers=`uname -r`
```
### 安装显卡驱动

```shell
pacman -S xf86-video-intel  #安装intel集显驱动
pacman -S xf86-video-amdgpu  #安装AMD集显驱动
pacman -S nvidia nvidia-utils  #安装NVIDIA独显驱动
```

### 安装蓝牙驱动

```shell
pacman -S bluez bluez-utils
systemctl start bluetooth.service
systemctl enable bluetooth.service
pacman -S broadcom-bt-firmware-git
modprobe -r btusb
modprobe btusb
sudo pacman -S pulseaudio-bluetooth  #安装蓝牙音频

nano /etc/pulse/system.pa 

#增加以下内容
load-module module-bluetooth-policy
load-module module-bluetooth-discover
```

### 安装声卡驱动

```shell
pacman -S alsa-utils
```

### 安装触摸板驱动

```shell
pacman -S xf86-input-synaptics
```

## 安装xorg

```shell
sudo pacman -S xorg xorg-server
```

### deepin

```shell
sudo pacman -S deepin deepin-extra
# 搜索,deepin是否自动安装lightdm
pacman -Qs lightdm
```

使用deepin的登录管理器

```shell
vim /etc/lightdm/lightdm.config
# 修改配置
greeter-session=lightdm-deepin-greeter

systemctl enable lightdm
```
