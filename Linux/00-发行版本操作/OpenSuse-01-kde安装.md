# 01-kde安装

#linux/program 

```shell
vim /etc/zypp/zypper.conf
# 修改
installRecommends = no

# 触摸板驱动 input-synaptics
zypper search input

# 中文字体 tff-dejavu wqy-microhei
# 网站 http://wenq.org/index.cgi?BitmapSong
sudo zypper in wqy-bitmap-fonts
```

安装并应用桌面

```shell
zypper in --no-recommends -t pattern kde-meta
zypper in --no-recommends dolphin dolphin-part-lang
zypper in --no-recommends kded-lang kde-cli-tools5-lang kdelibs4support-lang polkit-kde-agent-5-lang patterns-kde-kde_yast
zypper in --no-recommends plasma-framework-lang plasma5-desktop-emojier plasma5-desktop-lang plasma5-firewall plasma5-firewall-lang plasma5-integration-plugin-lang plasma5-workspace-lang
zypper in --no-recommends -t sddm sddm-kcm
systemctl enable sddm

cp /etc/systemd/system/default.target  /etc/systemd/system/default.target.bac
cp /usr/lib/systemd/system/graphical.target /etc/systemd/system/default.target
```

安装虚拟机驱动
```shell
zypper install kernel-desktop-devel
zypper install kernel-source kernel-syms
```

安装音频与输入法
```shell
pacman -S alsa-utils pulseaudio pulseaudio-alsa
pacman -S fcitx fcitx-rime fcitx-im kcm-fcitx


vim ~/xprofile
```

