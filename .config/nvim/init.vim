let g:startify_custom_header = [
 \ '                                        ▟▙            ',
 \ '                                        ▝▘            ',
 \ '██▃▅▇█▆▖  ▗▟████▙▖   ▄████▄   ██▄  ▄██  ██  ▗▟█▆▄▄▆█▙▖',
 \ '██▛▔ ▝██  ██▄▄▄▄██  ██▛▔▔▜██  ▝██  ██▘  ██  ██▛▜██▛▜██',
 \ '██    ██  ██▀▀▀▀▀▘  ██▖  ▗██   ▜█▙▟█▛   ██  ██  ██  ██',
 \ '██    ██  ▜█▙▄▄▄▟▊  ▀██▙▟██▀   ▝████▘   ██  ██  ██  ██',
 \ '▀▀    ▀▀   ▝▀▀▀▀▀     ▀▀▀▀       ▀▀     ▀▀  ▀▀  ▀▀  ▀▀',
 \ '',
 \]


if exists('+termguicolors')
 let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
 let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"
 set termguicolors
endif

let mapleader = " " " space is the leader key
let maplocalleader=" "
syntax on
filetype on

" sets
set encoding=utf-8
set wildmenu " autocompletion for commandmenu
set nu rnu
set tabstop=4 " four spaces tab
set expandtab " convert tabs to spaces
set shiftwidth=4 " indents of four spaces
set softtabstop=4 " backspace will remove tabs instead of space
set nowrap " no wrap lines
set mouse=a " enable use of the mouse
set showmatch " highlight matching brackets
set incsearch " search as characters are entered
set cpoptions+=x " stay at seach item when <esc>
set hlsearch " highlight all text matching current search pattern
set ignorecase " case insensitive search
set smartcase " case sensitive when uppercase
set backspace=indent,eol,start
set noswapfile " swap files won't be created
set nobackup " no backup
set scrolloff=6
set nowritebackup
set nohlsearch
set hidden
set autoindent
set smartindent
set cursorline "highlight current line
set clipboard+=unnamedplus
set updatetime=50
set conceallevel=0
set laststatus=0
set noshowcmd
set noshowmode
set cmdheight=1
set noruler
set list listchars=nbsp:¬,tab:»·,trail:·,extends:> " show whitespace chars
set formatoptions-=c formatoptions-=r formatoptions-=o " new line is not commented out
set guicursor+=i:ver100-iCursor


" keybinds
inoremap jj <Esc>
inoremap kk <Esc>
noremap <Leader>s :update<CR>
noremap <silent><Leader>l :noh<CR>

vnoremap <leader>p "_dP

noremap <silent><Leader>q :bd<CR>
noremap <silent><Leader><Leader> :bn<CR>
noremap <silent><Leader>p :bp<CR>

inoremap <C-H> <C-W>
nnoremap S :%s//gc<Left><Left><Left>

nmap <leader>c <Plug>Commentary
xmap <leader>c <Plug>Commentary
omap <leader>c <Plug>Commentary
nmap <leader>cc <Plug>CommentaryLine

map f <Plug>Sneak_s
map F <Plug>Sneak_S

noremap <silent><leader>git  :GFiles<CR>
nnoremap <silent><leader>t   :Files<CR>
nnoremap <silent><leader>f   :Lines<CR>
nnoremap <silent><leader>b   :Buffers<CR>
nnoremap <silent><leader>r   :History<CR>

nmap <silent><F6> :TagbarToggle<CR>
nnoremap <silent><Leader>g :Goyo<CR>


function! CustomColors()
    hi iCursor guibg=#e5c463
    hi CursorLine guibg=#373a45
    hi CursorLineNr guibg=NONE guifg=#e3e1e4 gui=bold
    hi LineNr guibg=NONE guifg=#707070
    hi Comment guifg=#707070
    hi Normal guibg=NONE
    hi EndOfBuffer guibg=NONE
    hi NonText guibg=NONE
    hi StatusLine guibg=NONE
    hi HighlightedyankRegion guibg=#506082
endfunction

" Goyo and Limelight
function! s:goyo_enter()
  if has('gui_running')
    set fullscreen
    set background=light
    set linespace=7
  elseif exists('$TMUX')
    silent !tmux set status off
  endif
endfunction

function! s:goyo_leave()
  if has('gui_running')
    set nofullscreen
    set background=dark
    set linespace=0
  elseif exists('$TMUX')
    silent !tmux set status on
  endif
endfunction

function! g:BuffetSetCustomColors()
  hi! BuffetCurrentBuffer guibg=NONE guifg=#e3e1e4 gui=bold
  hi! BuffetModCurrentBuffer guibg=NONE guifg=#e5c463
  hi! BuffetActiveBuffer guibg=NONE guifg=#707070
  hi! BuffetBuffer guibg=NONE guifg=#707070
  hi! BuffetTrunc guibg=NONE guifg=#707070
  hi! BuffetTab guibg=NONE guifg=#707070
  hi! BuffetModActiveBuffer guibg=NONE guifg=#e5c463
  hi! BuffetModBuffer guibg=NONE guifg=#707070
endfunction

fun! TrimWhitespace()
    let l:save = winsaveview()
    keeppatterns %s/\s\+$//e
    call winrestview(l:save)
endfun

augroup donut
    autocmd!
    autocmd FileType python map <buffer> <F5> :w<CR>:exec '!python' shellescape(@%, 1)<CR>
    autocmd FileType python imap <buffer> <F5> <esc>:w<CR>:exec '!python3' shellescape(@%, 1)<CR>

    autocmd BufWritePre * :call TrimWhitespace()

    autocmd InsertEnter * hi CursorLineNr guifg=#e5c463 | hi CursorLine guibg=#3c3c3c
    autocmd InsertLeave * hi CursorLineNr guifg=#e3e1e4 | hi CursorLine guibg=#373a45

    autocmd! User GoyoEnter nested call <SID>goyo_enter()
            \   | Limelight
    autocmd! User GoyoLeave nested call <SID>goyo_leave()
            \   | Limelight!
            \   | call CustomColors()
augroup END


call plug#begin()
    Plug 'junegunn/fzf.vim'
    Plug 'junegunn/goyo.vim'
    Plug 'junegunn/limelight.vim'
    Plug 'tpope/vim-fugitive' | Plug 'junegunn/gv.vim'
    Plug 'tpope/vim-surround'
    Plug 'tpope/vim-commentary'
    Plug 'machakann/vim-highlightedyank'
    Plug 'sainnhe/sonokai'
    Plug 'Yggdroot/indentLine'
    Plug 'justinmk/vim-sneak'
    Plug 'mhinz/vim-startify'
    Plug 'lervag/vimtex'
    Plug 'preservim/tagbar'
    Plug 'bagrat/vim-buffet'
    Plug 'vim-python/python-syntax'
call plug#end()

let g:sneak#label = 1
let g:sneak#use_ic_scs = 1
let g:sneak#s_next = 1

set nocompatible
let &rtp = '~/.vim/bundle/vimtex,' . &rtp
filetype plugin indent on
set iskeyword+=:
let g:tex_flavor = "latex"
let g:vimtex_view_method = 'zathura'

let g:sonokai_disable_italic_comment = 1
let g:limelight_conceal_guifg = 'DarkGray'
let g:highlightedyank_highlight_duration = 500
let g:python_highlight_all = 1
let g:fzf_preview_window = []
let g:buffet_always_show_tabline = 0
let g:buffet_tab_icon = ''
let g:buffet_separator = ''
let g:tagbar_autoclose = 1

colorscheme sonokai
call CustomColors()
