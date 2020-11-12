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
    set background=dark
    highlight HighlightedyankRegion cterm=reverse guibg=#505050
    hi CursorLine guibg=NONE
    hi CursorLineNr gui=bold guibg=NONE
    hi LineNr guifg=#454545
    hi Normal guibg=NONE
    hi EndOfBuffer guibg=NONE
    hi NonText guibg=NONE
    hi StatusLine guifg=#454545
endfunction

" Change Color when entering Insert Mode
autocmd InsertEnter * highlight  CursorLineNr guifg=#e5c463

" Revert Color to default when leaving Insert Mode
autocmd InsertLeave * highlight  CursorLineNr guifg=#e3e1e4

" keybindings
inoremap jj <Esc>
nnoremap <Leader>g :Goyo<CR>
nmap <F5> <Esc>:w<CR>:!clear;python %<CR> " exectute python
map <C-n> :NERDTreeToggle<CR>
nnoremap x "_x

nnoremap <leader>git      :GFiles<CR>
nnoremap <leader><leader> :Files<CR>
nnoremap <leader>C        :Colors<CR>
nnoremap <leader><CR>     :Buffers<CR>
nnoremap <leader>fl       :Lines<CR>
nnoremap <leader>ag       :Ag! <C-R><C-W><CR>
nnoremap <leader>m        :History<CR>

call plug#begin()
    Plug 'Yggdroot/indentLine'
	Plug 'justinmk/vim-sneak'
	Plug 'preservim/nerdtree'
	Plug 'junegunn/fzf.vim'
    Plug 'junegunn/goyo.vim'
    Plug 'junegunn/limelight.vim'
    Plug 'machakann/vim-highlightedyank'
    Plug 'tpope/vim-fugitive' | Plug 'junegunn/gv.vim'
    Plug 'sainnhe/sonokai'
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


"NERDTree
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in")
        \ | NERDTree | endif
autocmd BufEnter * if (winnr("$") == 1 
        \ && exists("b:NERDTree") 
        \ && b:NERDTree.isTabTree()) | q | endif

"sneak
let g:sneak#label = 1
let g:sneak#use_ic_scs = 1
let g:sneak#s_next = 1

let g:sonokai_disable_italic_comment = 1
let g:limelight_conceal_guifg = 'DarkGray'
let g:highlightedyank_highlight_duration = 350
let g:python_highlight_all = 1
call CustomColors()
