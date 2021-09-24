syntax on
noremap <C-u> <C-r>
noremap <C-r> <C-u>

set fileencodings=utf-8,ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set encoding=utf-8

" ȡ������ʱ��Сд
set ic
" ��������ʱ����
set hls

" set is

" ��ʾ�к�
set number
" ��ʾ��굱ǰλ��
set ruler
" ��������
set cindent
set tabstop=2
set shiftwidth=2

" ͻ����ʾ��ǰ��
set cursorline
" ���½���ʾ��ǰ vim ģʽ
set showmode
" �����۵�
set nofoldenable
" ����
set background=dark
" colorscheme solarized

" ״̬��
set laststatus=2      " ������ʾ״̬��
highlight StatusLine cterm=bold ctermfg=yellow ctermbg=blue

" ��ȡ��ǰ·������$HOMEת��Ϊ~
function! CurDir()
        let curdir = substitute(getcwd(), $HOME, "~", "g")
        return curdir
endfunction
set statusline=%n]%f%m%r%h\|pwd:\ %{CurDir()}\|%=\|%l,%c\ %p%%\|hex=%b%{((&fenc==\"\")?\"\":\"\|\".&fenc)}

noremap <c-g> :term lazygit<CR>
"noremap <c-g> :tabe<CR>:term lazygit<CR>
