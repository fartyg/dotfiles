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

let mapleader = " " " space is the leader key
let maplocalleader=" "
syntax on " syntax highlighting
filetype on
set wildmenu " autocompletion for commandmenu
set number relativenumber
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
set scrolloff=5 " Display 5 lines above/below the cursor when scrolling with a mouse.
set backspace=indent,eol,start
set noswapfile " swap files won't be created
set nobackup " no backup
set nowritebackup
set autoindent
set smartindent
set cursorline "highlight current line
set clipboard+=unnamedplus
set updatetime=300
set conceallevel=0
set laststatus=0
set noshowcmd
set noshowmode " hide mode text at the bottom
set cmdheight=1
set noruler

" keybindings
inoremap jj <Esc>
inoremap kk <Esc>
noremap <Leader>s :update<CR>
noremap <silent><Leader>q :bd<CR>
noremap <silent><Leader><Leader> :bn<CR>
noremap <silent><Leader>p :bp<CR>
noremap <silent><Leader>l :noh<CR>
inoremap <C-H> <C-W>

" m (move) is cut and d is actually delete with vim-cutlass
nnoremap m d
xnoremap m d
nnoremap mm dd
nnoremap M D

nmap <leader>c <Plug>Commentary
xmap <leader>c <Plug>Commentary
omap <leader>c <Plug>Commentary
nmap <leader>cc <Plug>CommentaryLine

nnoremap <silent><leader>git :GFiles<CR>
nnoremap <silent><leader>t   :Files<CR>
nnoremap <silent><leader>f   :Lines<CR>
nnoremap <silent><leader>b   :Buffers<CR>
nnoremap <silent><leader>r   :History<CR>

nnoremap <silent><Leader>g :Goyo<CR>

autocmd FileType python map <buffer> <F5> :w<CR>:exec '!python3' shellescape(@%, 1)<CR>
autocmd FileType python imap <buffer> <F5> <esc>:w<CR>:exec '!python3' shellescape(@%, 1)<CR>
nmap <silent><F6> :TagbarToggle<CR>

"terminal colors
if exists('+termguicolors')
 let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
 let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"
 set termguicolors
endif

function! CustomColors()
    hi CursorLine guibg=#373a45
    hi CursorLineNr guibg=NONE guifg=#e3e1e4 gui=bold
    hi LineNr guibg=NONE guifg=#606060
    hi Comment guifg=#606060
    hi Normal guibg=NONE
    hi EndOfBuffer guibg=NONE
    hi NonText guibg=NONE
    hi StatusLine guibg=NONE
endfunction

autocmd InsertEnter * highlight CursorLineNr guifg=#e5c463
autocmd InsertLeave * highlight CursorLineNr guifg=#e3e1e4

call plug#begin()
    Plug 'junegunn/fzf.vim'
    Plug 'junegunn/goyo.vim'
    Plug 'junegunn/limelight.vim'
    Plug 'tpope/vim-fugitive' | Plug 'junegunn/gv.vim'
    Plug 'tpope/vim-surround'
    Plug 'tpope/vim-commentary'
    Plug 'svermeulen/vim-cutlass'
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

"Goyo and Limelight
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

autocmd! User GoyoEnter nested call <SID>goyo_enter()
        \   | Limelight
autocmd! User GoyoLeave nested call <SID>goyo_leave() 
        \   | Limelight!
        \   | call CustomColors()

"sneak
let g:sneak#label = 1
let g:sneak#use_ic_scs = 1
let g:sneak#s_next = 1

"vimtex
set nocompatible
let &rtp = '~/.vim/bundle/vimtex,' . &rtp
filetype plugin indent on
set iskeyword+=:
let g:tex_flavor = "latex"
let g:vimtex_view_method = 'zathura'

" etc
let g:sonokai_disable_italic_comment = 1
let g:sonokai_transparent_background = 1
let g:limelight_conceal_guifg = 'DarkGray'
let g:highlightedyank_highlight_duration = 500
let g:python_highlight_all = 1
let g:fzf_preview_window = []
let g:buffet_always_show_tabline = 0
let g:buffet_tab_icon = ''
let g:buffet_separator = ''
let g:tagbar_autoclose = 1
highlight HighlightedyankRegion cterm=reverse gui=reverse

function! g:BuffetSetCustomColors()
  hi! BuffetCurrentBuffer guibg=NONE guifg=#e3e1e4 gui=bold
  hi! BuffetModCurrentBuffer guibg=NONE guifg=#e5c463
  hi! BuffetActiveBuffer guibg=NONE guifg=#606060
  hi! BuffetBuffer guibg=NONE guifg=#606060
  hi! BuffetTrunc guibg=NONE guifg=#606060
  hi! BuffetTab guibg=NONE guifg=#606060
  hi! BuffetModActiveBuffer guibg=NONE guifg=#e5c463
  hi! BuffetModBuffer guibg=NONE guifg=#606060
endfunction

colorscheme sonokai
call CustomColors()
