# DWM， rofi, st

#linux #linux/program 

如果没有安装显卡驱动，需要安装

```shell
route add default gw 10.0.2.7
route -n
```

git 经行版本控制

```shell
vim .gitignore
*.o
*.orig
*.rej

git add .
git status
git commit -m "first built"
```

## 下载软件与依赖

```shell
sudo pacman -S xorg-server xorg-apps xorg-xinit
sudo pacman -S noto-fonts-cjk
sudo pacman -S wqy-microhei
sudo pacman -S w3m #终端网页浏览器
sudo pacman -S lazygit
```

```shell
cd ~
cp /etc/X11/xinit/xinitrc ~/myconfig/.xinitrc
```

删除`# twm &`及以下的配置，然后添加dwm启动

```shell
vim  ~/myconfig/.xinitrc



#picom
picom &
## habak
while habak -mC -hi ~/myconfig/wallpaper/   #让habak从你的壁纸目录中随机选择一张屏幕壁纸显示
do
sleep 600   #让habak每隔10分钟随机切换一张屏幕壁纸
done &
 #自动自动开启数字键盘
numlockx &
## dwm
exec dwm
#xrandr 设置分辨率问题
# xrandr --auto --output HDMI1 --same-as eDP1 --size 1920*1080
# xrandr命令设置屏幕分辨率以及多屏
xrandr --output Virtual1 --mode 1680x1050 --rate 60
xrandr --output Virtual1 --size 1900x1050 --rate 60
xrandr --auto --size 1800x900
```

### 下载其他配套软件

```shell
sudo pacman -S rofi
sudo pacman -S habak
sudo pacman -S picom
sudo pacman -S x11-apps/xsetroot
sudo pacman -S numlockx
sudo pacman -S nm-applet  #网络管理
```

### dwm

```shell
git clone https://git.suckless.org/dwm --depth=1
cd dwm
make
mv ~/dwm/config.def.h ~/dwm/config.def.h.bak
vim config.h

# 编辑这两行
static const char *dmenucmd[] = { "rofi","-show","run", NULL };
###static const char *termcmd[]  = { "zsh", NULL };

sudo make clean install

# 显示的结果为下

mkdir -p /usr/local/bin
cp -f dwm /usr/local/bin
chmod 755 /usr/local/bin/dwm
mkdir -p /usr/local/share/man/man1
sed "s/VERSION/6.2/g" < dwm.1 > /usr/local/share/man/man1/dwm.1
chmod 644 /usr/local/share/man/man1/dwm.1
```

#### patches

```shell
mv config.def.h config.def.h.bak
patches < 01

#有几行我觉得不用加
#  		die("error, cannot allocate color '%s'", clrname);
# +
# +	dest->pixel |= 0xff << 24;

```


### st

```shell
# 需要 libx11-dev libft-dev
git clone https://git.suckless.org/st --depth=1
cd ~
vim config.mk
#改变下面
X11INC = /usr/X11R6/include
X11LIB = /usr/X11R6/lib
#变为
X11INC = /usr/include/X11
X11LIB = /usr/include/X11

make
mv ~/st/config.def.h ~/st/config.def.h.bak
mkdir patches
# 将下载好的patches放到这个文件见

# 开始对st经行配置 
vim config.h
# 在下面这行改字体
static chat *font = .......pixelsize=28
patch < patches/st-alpha
patch < patches/st-anysize-0.8.1.diff

sudo make clean install
```

## 配置X11,并启动dwm

```shell
ln -sf ~/myconfig/.xinitrc ~/.xinitrc
startx
```

### 增加配套软件

```shell
# 输入法
sudo pacman -S fcitx-im fcitx-googlepinyin fcitx-configtool
# 具体配置可查archwiki 搜索fcitx
vim ~/.xinitrc
# 在最顶端填写
# fcitx
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx


# 运行
fcitx
fcitx-configtool
```

```shell
```