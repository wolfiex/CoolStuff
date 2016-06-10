" Vim RC:  Dan Ellis 2016

set t_Co=256

syntax on
set background=dark
set ruler                     " show the line number on the bar
set more                      " use more prompt
set autoread                  " watch for file changes
set number                    " line numbers
colorscheme danscolourscheme
"DoMatchParen
filetype plugin indent on
" show existing tab with 4 spaces width
set tabstop=4
" when indenting with '>', use 4 spaces width
set shiftwidth=4
" On pressing tab, insert 4 spaces
set expandtab
"only care about whitespare in normal vim, not vimdiff. 
if &diff
    " diff mode
    set diffopt+=iwhite
endif


" Save Page using ctrl-  
:map<c-d> <Esc>:w<CR>
:imap<c-d> <Esc>:w<CR>
" Save and Close
:imap <c-x> <Esc>:x<CR>
:map <c-x> <Esc>:x<CR>

