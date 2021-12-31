# lazygit

#linux #linux/program/shell 

>`https://github.com/jesseduffield/lazygit/releases`

```shell
wget https://github.com/jesseduffield/lazygit/releases/download/v0.31.4/lazygit_0.31.4_Linux_x86_64.tar.gz -O lazygit.tgz 
tar xvf lazygit.tgz
sudo mv ./lazygit /usr/local/bin/
```

## git

```shell
git config --global http.proxy 'socks5://192.168.56.1:7890'
git config --global https.proxy 'socks5://192.168.56.1:1080'
git config --global user.name
git config --global user.email
```

## Files

- A : 提交到上一次Commits

### Merge

- b : 选择所有的更改

## branches

- M : 合并分支

## commits

- r : 重命名
- g ：重置为以前提交的版本
- c : 复制提交， 到barches 后按v粘贴提交
- s : 与下面的提交(上一次提交)合并
- `ctrl+f` : 查看当前文件的所有提交记录
- W : 对比提交

> custom Patch模式

- 选中更改按空格,然后按`ctrl+p`
  - remove patch from : 删除更改
  - pull patch out into index : 退回到未提交的工作文件
  - pull patch into new commit : 将选中的生成一个新的提交
- 在另一个commits上按`ctrl+p`可以选择将选中内容换到改commits中

### Reflog

- g : 恢复

## stash

- g : 恢复

## 配置

- Linux: ~/.config/jesseduffield/lazygit/config.yml
- MacOS: ~/Library/Application Support/jesseduffield/lazygit/config.yml
- Windows: %APPDATA%\jesseduffield\lazygit\config.yml

```shell
ln -sf ~/myconfig/lazygit.yml ~/.config/jesseduffield/lazygit/config.yml
ln -sf ~/myconfig/lazygit.yml ~/.config/lazygit/config.yml
Packages (1) diff-so-fancy-1.3.0-1
```

```yml
git:
  paging:
    colorArg: always
    pager: diff-so-fancy
gui:
  commitlength:
    show: true
  mouseevents: false
  scrollheight: 2
  scrollpastbottom: true
  theme:
    lightTheme: false
    activeBorderColor:
      - cyan
      - bold
    inactiveBorderColor:
      - white
    optionsTextColor:
      - blue
    selectedLineBgColor:
      - default
    selectedRangeBgColor:
      - blue
```

需要安装ruby 后 `brew install delta`

```yml
git:
  autofetch: true
  merging:
    manualcommit: false
  skiphookprefix: WIP
  paging:
    colorArg: always
    pager: delta --dark --paging=never --24-bit-color=never --theme="OneHalfDark"
gui:
  commitlength:
    show: true
  mouseevents: false
  scrollheight: 2
  scrollpastbottom: true
  theme:
    lightTheme: false
    activeBorderColor:
      - cyan
      - bold
    inactiveBorderColor:
      - white
    optionsTextColor:
      - blue
    selectedLineBgColor:
      - default
    selectedRangeBgColor:
      - blue
```

## 快捷键

### range

```rc.conf
map <c-g> shell lazygit
```

### fish

alt+g

```fish_prompt.fish
bind \eg lazygit
```

### vim

```vimrc
noremap <c-g> :term lazygit<CR>
"noremap <c-g> :tabe<CR>:-tabmove<CR>:term lazygit<CR>
```

### zsh

```shell
function zle_eval {
    echo -en "\e[2K\r"
    eval "$@"
    zle redisplay
}

function openlazygit {
    zle_eval lazygit
}

zle -N openlazygit; bindkey "^G" openlazygit

function openlazynpm {
    zle_eval lazynpm
}

zle -N openlazynpm; bindkey "^N" openlazynpm
'''
