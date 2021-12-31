# 快捷键总结
## st
| key         | use         | [=] | key       | use         |
| ----------- | ----------- | --- | --------- | ----------- |
| alt + PU,PD | scroll page | [=] | alt + j,k | scroll line |
| alt + l     | highli url  | [=] | alt + C-q | openurlcmd  |
| alt + y     | copyurlcmd  | [=] | alt + o   | copyoutput  |


# xorg安装

#linux/program 

> suse

```shell
# zypper in xdm xorg-x11-server xorg-x11-server-Xvfb xorg-x11-driver-video xorg-x11-fonts-core xinit
# zypper in --no-recommends -t pattern x11
zypper in xorg-x11-server xorg-x11-server-Xvfb xorg-x11-driver-video xorg-x11-fonts-core xinit 

# 安装图形界面模块
zypper in xf86-input-evdev
zypper in xf86-input-keyboard xf86-input-joystick xf86-input-mouse xf86-input-synaptics xf86-input-vmmouse xf86-input-libinput xf86-input-vmmouse xf86-input-void

# 显卡选装
zypper in xf86-video-vesa xf86-video-vmware xf86-video-intel xf86-video-amdgpu xf86-video-ati xf86-video-nv

# 设置initx
vim /etc/permissions.local
# ------
/usr/bin/Xorg                 root:root       4777

chkstat --system --set
chkstat --system /usr/bin/Xorg

# 设置startx后执行程序
echo '#!/bin/sh' >> ~/.xinitrc
sudo chmod +x ~/.xinitrc
vim ~/.xinitrc
```

## lightdm
```shell
zypper in lightdm-slick-greeter-branding-openSUSE
update-alternatives --list default-displaymanager
update-alternatives --config default-displaymanager
update-alternatives --set default-displaymanager /usr/lib/X11/displaymanagers/<choice>
systemctl set-default runlevel5.target
```

### arch

你可以通过更改配置文件的 `[Seat:*]` 部分设置 greeter:

```shell
ls -1 /usr/share/xgreeters/
vim /etc/lightdm/lightdm.conf
[Seat:*]
...
greeter-session=lightdm-yourgreeter-greeter
```

# st

## 设置字体
![00.安装后一些设置](./00.安装后一些设置.md#设置字体)
- `vim conf.h`
```c
static char *font = "Anonymice Nerd Font Mono":pixelsize=24:antialias=true:autohint=true";
```

## 安装补丁
```shell
pacman -Ss patch
zypper in patch

patch < st-alpha-0.8.2.diff 
patch < st-anysize-0.8.4.diff #占满屏幕
patch < st-dracula-0.8.2.diff 
patch < st-scrollback-20210507-4536f46.diff #向上翻滚
patch < st-copyurl-0.8.4.diff #高亮链接
patch < st-lukesmith-externalpipe\(if_you_have_scrollback\).diff #控制输出
patch < st-dynamic-cursor-color-0.8.4.diff #光标颜色换色
patch < st-desktopentry-0.8.4.diff 
patch < st-fontfix.diff 
```

## 修改参数
`vim config.def.h`
```c
// st-alpha-0.8.2.diff 
/* bg opacity */  
float alpha = 0.7;
```


## 设置快捷键
`vim config.def.h`
```c
static MouseShortcut mshortcuts[] = {
 /* mask                 button   function        argument       release */
 { XK_ANY_MOD, Button2, selpaste, {.i = 0}, 1 },
 { XK_ANY_MOD, Button4, kscrollup, {.i = 1}, 1 },
 { XK_ANY_MOD, Button5, kscrolldown, {.i = 1}, 1 },
 // { ShiftMask,            Button4, ttysend,        {.s = "\033[5;2~"} },
 // { XK_ANY_MOD,           Button4, ttysend,        {.s = "\031"} },
 // { ShiftMask,            Button5, ttysend,        {.s = "\033[6;2~"} },
 // { XK_ANY_MOD,           Button5, ttysend,        {.s = "\005"} },
};

#define MODKEY Mod1Mask
#define TERMMOD (ControlMask|ShiftMask)

static Shortcut shortcuts[] = {
 // 自定义快捷键
 // 滚动
 { MODKEY, XK_Up, kscrollup, {.i = 1} },
 { MODKEY, XK_Down, kscrolldown, {.i = 1} },
 { MODKEY, XK_j, kscrollup, {.i = -1} },
 { MODKEY, XK_k, kscrolldown, {.i = -1} },
 // url
 { MODKEY, XK_l, copyurl, {.i = 0} },
 // 复制版
 { MODKEY|ControlMask, XK_q, externalpipe, {.v = openurlcmd } },
 { MODKEY, XK_y, externalpipe, {.v = copyurlcmd } },
 { MODKEY, XK_o, externalpipe, {.v = copyoutput } },
};
```

## 安装
```
sudo make clean install
rm config.h
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