
Vim 的全局配置一般在`/etc/vim/vimrc`或者`/etc/vimrc`

```shell

cp .vimrc ~/myconfig
ln -sf ~/myconfig/.vimrc  ~/.vimrc
```

- `G`: 文档末尾
- `gg`: 文档开头
- `L`: 屏幕最低
- `H`: 屏幕最上
- `$`: 行尾
- `^`: 行首
- `ctrl+f`: 下翻
- `ctrl+b`: 上翻

- `J`: 两行合并
- `K`: 帮助

## 分屏

```vim
:new
#2. 打开当前文件
#命令（水平）：
[CTRL] [W] s

#命令（垂直）：
[CTRL] [W] v

#3. 打开任意文件
#命令（水平）：
:split [FILENAME]
:sp [FILENAME]
    
#命令（垂直）：
:vsplit [FILENAME]
:vs [FILENAME]
```

| 命令（快捷键） | 说明               |
| -------------- | ------------------ |
| [CTRL]  [W]  + | 扩大窗口           | 
| [CTRL]  [W]  - | 缩小窗口           |
| [CTRL]  [W]  h | 跳转到左边的窗口   |
| [CTRL]  [W]  j | 跳转到下边的窗口   |
| [CTRL]  [W]  k | 跳转到上边的窗口   |
| [CTRL]  [W]  l | 跳转到右边的窗口   |
| [CTRL]  [W]  t | 跳转到最顶上的窗口 |
| [CTRL]  [W]  b | 跳转到最顶下的窗口 |