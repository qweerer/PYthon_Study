# ranger

## 需要的前置

```shell
apk add file bat
ranger --copy-config=all
```


## 配置修改

修改默认文本编辑器
```shell
echo export EDITOR=/usr/bin/vim >> ~/.bashrc
```

### `rc.conf`

```shell
#显示边框线
set draw_borders true
## 仅预览2MB以下的文件
set preview_max_size 2048000
## 修改配色风格
set colorscheme jungle
## 行号显示
set line_numbers relative
## 行号设置成从1开始
set one_indexed true
## 没预览时不折叠预览区
set collapse_preview false
## 自动换行
set wrap_plaintext_previews false
### git显示
set vcs_aware true
```

## 使用图标

>下载[nerd字体](https://www.nerdfonts.com/font-downloads)并启用

```shell
git clone https://github.com/alexanderjeurissen/ranger_devicons ~/.config/ranger/plugins/ranger_devicons
echo "default_linemode devicons" >> $HOME/.config/ranger/rc.conf
```

## 快捷键
- `空格` 选择
- `v` 全选
- `:bulkrename` 在vim中重命名
- `w` 查看后台任务
- `a` 重命名
- `S` shell进入文件夹

## root用户启用预览

可能是为了安全考虑，ranger默认在root用户中不启动预览功能。如何在root用户中也开启预览呢？
我在这里找到了解决办法：https://bbs.archlinux.org/viewtopic.php?id=183674

具体操作如下：

- ranger按gR 进入ranger安装目录，找到ranger/core/main.py
- 搜索`Running as root, disabling the file previews.`
- 改`if fm.username == 'root':`中的`root`为任意值

# bat

```shell
bat cache --target ~/.config/bat/ --build
bat --list-languages
bat --config-file
# 指定config
export BAT_CONFIG_PATH="~/.config/bat/bat.conf"
bat --generate-config-file

--map-syntax "**/*.conf:Bourne Again Shell (bash)"
```
