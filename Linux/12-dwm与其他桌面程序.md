# xorg安装

#linux/program 

## suse

```shell
# zypper in xdm xorg-x11-server xorg-x11-server-Xvfb xorg-x11-driver-video xorg-x11-fonts-core xinit
# zypper in --no-recommends -t pattern x11
zypper in xorg-x11-server xorg-x11-server-Xvfb xorg-x11-driver-video xorg-x11-fonts-core xinit 

# 安装图形界面模块
zypper in xf86-input-evdev
zypper in xf86-input-keyboard xf86-input-joystick xf86-input-mouse xf86-input-synaptics xf86-input-vmmouse xf86-input-libinput xf86-input-vmmouse xf86-input-void

# 显卡选装
zypper in xf86-video-vesa xf86-video-vmware xf86-video-intel xf86-video-amdgpu xf86-video-ati xf86-video-nv
```

# dwm



```
vim  /usr/share/xsessions/dwm.desktop

[Desktop Entry]
Encoding=UTF-8
Name=Dwm
Comment=Dynamic window manager
Exec=dwm
Icon=dwm
Type=XSession
```