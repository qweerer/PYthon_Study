" 操作建议
" 1. cw 替换下个单词
" 2. ciw 替换这个单词
" 3. ci" 替换引号中的内容
" 4. di" 删除引号中的内容
" 5. fv 跳到下一个v
" 6. dfv 删除到下一个v
" =====================
" 折叠:indent
" zc 折叠
" zC 对所在范围内所有嵌套的折叠点进行折叠
" zo 展开折叠
" zO 对所在范围内所有嵌套的折叠点展开
" [z 到当前打开的折叠的开始处。
" ]z 到当前打开的折叠的末尾处。
" zj 向下移动。到达下一个折叠的开始处。关闭的折叠也被计入。
" zk 向上移动到前一折叠的结束处。关闭的折叠也被计入。
" 折叠:marker
" zf　创建折叠，比如在marker方式下：
"         zf56G，创建从当前行起到56行的代码折叠；
"         10zf或10zf+或zf10↓，创建从当前行起到后10行的代码折叠。
"         10zf-或zf10↑，创建从当前行起到之前10行的代码折叠。
"         在括号处zf%，创建从当前行起到对应的匹配的括号上去（（），{}，[]，<>等）。
" zd  删除 (delete) 在光标下的折叠。仅当 'foldmethod' 设为 "manual" 或 "marker" 时有效。
" zD  循环删除 (Delete) 光标下的折叠，即嵌套删除折叠。仅当 'foldmethod' 设为 "manual" 或 "marker" 时有效。
" zE  除去 (Eliminate) 窗口里“所有”的折叠。仅当 'foldmethod' 设为 "manual" 或 "marker" 时有效。

" 恢复快捷键
noremap <C-u> <C-r> "恢复操作
noremap <C-r> <C-u>
noremap zz u
noremap Z <C-r>
" 代码折叠
noremap zi :set foldmethod=indent<CR>
noremap zm :set foldmethod=marker<CR>
" 翻页快捷键
noremap j k
noremap k j
noremap <C-h> ^
noremap <C-l> <end>
noremap <C-j> ^
noremap <C-k> <end>
" noremap <C-j> <C-f>
" noremap <C-k> <C-b>
noremap J 25k
noremap K 25j
"保存快捷键
map s <nop>
noremap ss :w<CR>
"取消高亮
noremap \/ :nohlsearch<CR>
"分屏
noremap \h :set nosplitright<CR>:vsplit<CR>
noremap \l :set splitright<CR>:vsplit<CR>
noremap \j :set nosplitbelow<CR>:split<CR>
noremap \k :set splitbelow<CR>:split<CR>
noremap \a <C-w>h
noremap \d <C-w>l
noremap \w <C-w>j
noremap \s <C-w>k
" 标签
noremap \n :tabe<CR>
noremap \q :-tabnext<CR>
noremap \e :+tabnext<CR>

imap jk <Esc>

set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8

" 取消查找时大小写
" set ic
set ignorecase
set smartcase
" 开启查找时高亮
set hlsearch
set incsearch
exec "nohlsearch"

" set is
" 如果退格键无法正常使用
set backspace=indent,eol,start
" 显示行号
set number
set relativenumber
" 显示光标当前位置
set ruler
" 设置缩进
set cindent
set tabstop=4
set shiftwidth=4

"设置换行
set wrap

" 突出显示当前行
set cursorline
" 左下角显示当前 vim 模式
set showmode
set showcmd
" vim指令有选项
set wildmenu

" 代码折叠
set nofoldenable
set foldmethod=indent

" 重新进入记住位置
au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif



### 以下与插件冲突
" 主题
set background=dark
" colorscheme zellner
" colorscheme ron/koehler

# 高亮
syntax on


" 状态栏
set laststatus=2      " 总是显示状态栏
highlight StatusLine cterm=bold ctermfg=yellow ctermbg=blue
" 获取当前路径，将$HOME转化为~
function! CurDir()
        let curdir = substitute(getcwd(), $HOME, "~", "g")
        return curdir
endfunction
"set statusline=[%n]\ %f%m%r%h\ \|\ \ pwd:\ %{CurDir()}\ \ \|%=\|\ %l,%c\ %p%%\ \|\ ascii=%b,hex=%b%{((&fenc==\"\")?\"\":\"\ \|\ \".&fenc)}\ \|\ %{$USER}\ @\ %{hostname()}\
"自己
set statusline=%n]%f%m%r%h\|pwd:\ %{CurDir()}\|%=\|%l,%c\ %p%%\|hex=%b%{((&fenc==\"\")?\"\":\"\|\".&fenc)}

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"sudo vi /etc/vimrc
set fileencodings=utf-8,gb2312,gbk,gb18030
set termencoding=utf-8
set encoding=prc

" 状态栏
set laststatus=2      " 总是显示状态栏
highlight StatusLine cterm=bold ctermfg=yellow ctermbg=blue
" 获取当前路径，将$HOME转化为~
function! CurDir()
        let curdir = substitute(getcwd(), $HOME, "~", "g")
        return curdir
endfunction
set statusline=%n]%f%m%r%h\|pwd:\ %{CurDir()}\|%=\|%l,%c\ %p%%\|\@%{$USER}
