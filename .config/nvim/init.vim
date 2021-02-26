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

set termguicolors
let mapleader = " " " space is the leader key
let maplocalleader=" "
filetype on

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
set updatetime=50
set clipboard+=unnamedplus
set conceallevel=0
set laststatus=0
set noshowcmd
set noshowmode
set cmdheight=1
set noruler
set list listchars=nbsp:¬,tab:»·,trail:·,extends:> " show whitespace chars
set fillchars+=vert:\ 
set formatoptions-=c formatoptions-=r formatoptions-=o " new line is not commented out
set splitbelow
set splitright


" ctrl + backspace removes word
inoremap <C-H> <C-W>

nnoremap S :%s//gc<Left><Left><Left>
inoremap jj <Esc>
noremap <Leader>s :update<CR>
noremap <silent><Leader>l :noh<CR>

nnoremap <cr> <c-w>w
nnoremap <silent><leader>v   :vsplit<CR>
nnoremap <silent><leader>h   :split<CR>
noremap <silent><Leader>q :bd<CR>
noremap <silent><Leader><Leader> :bn<CR>

nmap <leader>c <Plug>Commentary
xmap <leader>c <Plug>Commentary
omap <leader>c <Plug>Commentary
nmap <leader>cc <Plug>CommentaryLine

map f <Plug>Sneak_s
map F <Plug>Sneak_S

" move (vim-cutlass)
noremap <Leader>m m
nnoremap m d
xnoremap m d
nnoremap mm dd
nnoremap M D

nmap <silent><F6> :TagbarToggle<CR>
nnoremap <silent><Leader>g :Goyo<CR>

noremap <silent><leader>git  :GFiles<CR>
nnoremap <silent><leader>t   :Files<CR>
nnoremap <silent><leader>f   :Lines<CR>
nnoremap <silent><leader>b   :Buffers<CR>
nnoremap <silent><leader>r   :History<CR>

nnoremap <silent> gd <cmd>lua vim.lsp.buf.definition()<CR>
nnoremap <silent> gh     <cmd>lua vim.lsp.buf.hover()<CR>
nnoremap <silent> gD    <cmd>lua vim.lsp.buf.implementation()<CR>
nnoremap <silent> <c-k> <cmd>lua vim.lsp.buf.signature_help()<CR>
nnoremap <silent> 1gD   <cmd>lua vim.lsp.buf.type_definition()<CR>
nnoremap <silent> gr    <cmd>lua vim.lsp.buf.references()<CR>
nnoremap <silent> g0    <cmd>lua vim.lsp.buf.document_symbol()<CR>
nnoremap <silent> gW    <cmd>lua vim.lsp.buf.workspace_symbol()<CR>

function! CustomColors()
    hi iCursor guibg=#e5c463
    hi vCursor guibg=#ab9df2
    hi CursorLine guibg=#373a45
    hi CursorLineNr guibg=NONE guifg=#e3e1e4 gui=bold
    hi LineNr guibg=NONE guifg=#707070
    hi SignColumn guibg=NONE
    hi Comment guifg=#707070
    hi Normal guibg=NONE
    hi Visual guibg=#543a59
    hi EndOfBuffer guibg=NONE
    hi NonText guibg=NONE
    hi StatusLine guibg=NONE
    set guicursor+=i:ver100-iCursor
    set guicursor+=v:block-vCursor
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


au VimLeave * set guicursor=a:ver100

autocmd FileType python map <buffer> <F5> :w<CR>:exec '!python' shellescape(@%, 1)<CR>
autocmd FileType yaml setlocal ts=2 sts=2 sw=2 expandtab

autocmd InsertEnter * hi CursorLineNr guifg=#e5c463 | hi CursorLine guibg=#3c3c3c
autocmd InsertLeave * hi CursorLineNr guifg=#e3e1e4 | hi CursorLine guibg=#373a45

autocmd! User GoyoEnter nested call <SID>goyo_enter()
        \   | Limelight
autocmd! User GoyoLeave nested call <SID>goyo_leave()
        \   | Limelight!
        \   | call CustomColors()

augroup highlight_yank
    autocmd!
    au TextYankPost * silent! lua vim.highlight.on_yank{higroup="IncSearch", timeout=350}
augroup END


call plug#begin()
    Plug 'neovim/nvim-lspconfig'
    Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
    Plug 'junegunn/fzf.vim'
    Plug 'junegunn/goyo.vim'
    Plug 'junegunn/limelight.vim'
    Plug 'tpope/vim-fugitive' | Plug 'junegunn/gv.vim'
    Plug 'tpope/vim-surround'
    Plug 'tpope/vim-repeat'
    Plug 'tpope/vim-commentary'
    Plug 'svermeulen/vim-cutlass'
    Plug 'sainnhe/sonokai'
    Plug 'Yggdroot/indentLine'
    Plug 'justinmk/vim-sneak'
    Plug 'mhinz/vim-startify'
    Plug 'lervag/vimtex'
    Plug 'preservim/tagbar'
    Plug 'bagrat/vim-buffet'
call plug#end()

" sneak
let g:sneak#label = 1
let g:sneak#use_ic_scs = 1
let g:sneak#s_next = 1

" vimtex
set nocompatible
let &rtp = '~/.vim/bundle/vimtex,' . &rtp
filetype plugin indent on
set iskeyword+=:
let g:tex_flavor = "latex"
let g:vimtex_view_method = 'zathura'

" other
let g:python_highlight_all = 1
let g:limelight_conceal_guifg = 'DarkGray'
let g:fzf_preview_window = []
let g:buffet_tab_icon = ''
let g:buffet_separator = ''
let g:tagbar_autoclose = 1
let g:indentLine_char = '⦙'

" startify
let g:startify_lists = [
        \ { 'type': 'bookmarks', 'header': ['   Bookmarks']},
        \ { 'type': 'files',     'header': ['   MRU']},
\ ]

let g:startify_bookmarks = [
        \ {'x': '~/Documents/notes.md'},
        \ {'z': '~/.zshrc'},
        \ {'a': '~/.config/alacritty/alacritty.yml'},
        \ {'c': '~/.config/i3/config'},
        \ {'n': '~/.config/nvim/init.vim'},
        \ {'m': '~/.config/mpv/mpv.conf'},
        \ {'p': '~/.config/picom.conf'},
        \ {'r': '~/.config/rofi/config.rasi'},
\ ]

let g:startify_skiplist = ['^/tmp']
for d in g:startify_bookmarks
    for v in values(d)
        call add(g:startify_skiplist, v)
    endfor
endfor


colorscheme sonokai
call CustomColors()


" nvim 0.5
lua <<EOF
require'nvim-treesitter.configs'.setup {
-- Modules and its options go here
highlight = { enable = true },
incremental_selection = { enable = true },
textobjects = { enable = true },
}
EOF

lua << EOF
require("lspconfig").pyls.setup{}
EOF

set completeopt-=preview

" use omni completion provided by lsp
autocmd Filetype python setlocal omnifunc=v:lua.vim.lsp.omnifunc
