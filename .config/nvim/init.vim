let mapleader = " " " space is the leader key
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

"terminal colors
if exists('+termguicolors')
 let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
 let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"
 set termguicolors
endif

function! CustomColors()
    colorscheme sonokai
    highlight HighlightedyankRegion cterm=reverse gui=reverse
    hi CursorLine guibg=#373a45
    hi CursorLineNr guibg=NONE guifg=#e3e1e4 gui=bold
    hi LineNr guibg=NONE guifg=#909090
    hi Comment guifg=#909090
    "hi Normal guibg=NONE
    "hi EndOfBuffer guibg=NONE
    "hi NonText guibg=NONE
    "hi StatusLine guibg=NONE
endfunction

" Change Color when entering Insert Mode
autocmd InsertEnter * highlight  CursorLineNr guifg=#e5c463

" Revert Color to default when leaving Insert Mode
autocmd InsertLeave * highlight  CursorLineNr guifg=#e3e1e4

" keybindings
noremap <Leader>s :update<CR>
noremap <Leader>q :bd<CR>
noremap <silent> <Leader><Leader> :bn<CR>
noremap <silent> <Leader>p :bp<CR>
noremap <silent> <Leader>l :noh<CR>
inoremap jj <Esc>
nnoremap <silent> <Leader>g :Goyo<CR>
nnoremap x "_x
nmap <F6> :TagbarToggle<CR>
autocmd FileType python map <buffer> <F5> :w<CR>:exec '!python3' shellescape(@%, 1)<CR>
autocmd FileType python imap <buffer> <F5> <esc>:w<CR>:exec '!python3' shellescape(@%, 1)<CR>

nnoremap <leader>git      :GFiles<CR>
nnoremap <leader>t        :Files<CR>
nnoremap <leader>f        :Lines<CR>
nnoremap <leader>b        :Buffers<CR>
nnoremap <leader>r        :History<CR>

function! g:BuffetSetCustomColors()
  hi! BuffetCurrentBuffer guibg=NONE guifg=#e3e1e4 gui=bold
  hi! BuffetModCurrentBuffer guibg=NONE guifg=#e5c463
  hi! BuffetActiveBuffer guibg=NONE guifg=#909090
  hi! BuffetBuffer guibg=NONE guifg=#909090
  hi! BuffetTrunc guibg=NONE guifg=#909090
  hi! BuffetTab guibg=NONE guifg=#909090
  hi! BuffetModActiveBuffer guibg=NONE guifg=#e5c463
  hi! BuffetModBuffer guibg=NONE guifg=#909090
endfunction

call plug#begin()
    Plug 'Yggdroot/indentLine'
    Plug 'justinmk/vim-sneak'
    Plug 'junegunn/fzf.vim'
    Plug 'mhinz/vim-startify'
    Plug 'junegunn/goyo.vim'
    Plug 'preservim/tagbar'
    Plug 'junegunn/limelight.vim'
    Plug 'machakann/vim-highlightedyank'
    Plug 'tpope/vim-fugitive' | Plug 'junegunn/gv.vim'
    Plug 'sainnhe/sonokai'
    Plug 'bagrat/vim-buffet'
    Plug 'vim-python/python-syntax'
call plug#end()

"Goyo and Limelight
"let g:limelight_conceal_guifg='#565656'
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

let g:fzf_preview_window = []
let g:tagbar_autoclose = 1
let g:sonokai_disable_italic_comment = 1
let g:sonokai_transparent_background = 1
let g:limelight_conceal_guifg = 'DarkGray'
let g:highlightedyank_highlight_duration = 500
let g:python_highlight_all = 1
let g:buffet_always_show_tabline = 0
let g:buffet_tab_icon = ''
let g:buffet_separator = ''
call CustomColors()
