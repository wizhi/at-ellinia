call plug#begin(stdpath('data') . '/plugged')

Plug 'https://github.com/sheerun/vim-polyglot'
Plug 'https://github.com/vim-airline/vim-airline'
Plug 'https://github.com/bling/vim-bufferline'
Plug 'https://github.com/junegunn/fzf'
Plug 'https://github.com/junegunn/fzf.vim'
Plug 'https://github.com/preservim/nerdtree'
Plug 'https://github.com/Xuyuanp/nerdtree-git-plugin'
Plug 'https://github.com/tpope/vim-fugitive'
Plug 'https://github.com/OmniSharp/omnisharp-vim'
Plug 'https://github.com/dense-analysis/ale'
Plug 'https://github.com/ncm2/ncm2'
Plug 'https://github.com/ncm2/ncm2-path'
Plug 'https://github.com/roxma/nvim-yarp'
Plug 'https://github.com/ervandew/supertab'

call plug#end()

set updatetime=100
set completeopt=noinsert,menuone,noselect
set relativenumber
set wildignore=""

function! UseTabs()
	set tabstop=4	  " Size of a hard tabstop (ts).
	set shiftwidth=4  " Size of an indentation (sw).
	set noexpandtab   " Always uses tabs instead of space characters (noet).
	set autoindent	  " Copy indent from current line when starting a new line (ai).

	autocmd BufWrite * retab!
endfunction

function! UseSpaces()
	set tabstop=4	  " Size of a hard tabstop (ts).
	set shiftwidth=4  " Size of an indentation (sw).
	set expandtab	  " Always uses spaces instead of tab characters (et).
	set softtabstop=0 " Number of spaces a <Tab> counts for. When 0, featuer is off (sts).
	set autoindent	  " Copy indent from current line when starting a new line.
	set smarttab	  " Inserts blanks on a <Tab> key (as per sw, ts and sts).

	autocmd BufWrite * retab
endfunction

call UseTabs()

let g:airline_extensions = ['bufferline']
let g:airline#extensions#bufferline#enabled = 1
let g:airline#extensions#bufferline#overwrite_variables = 1
let g:bufferline_echo = 0

let g:SuperTabDefaultCompletionType = "<C-n>"

let g:ale_linters = {
			\  'cs': ['OmniSharp'] }
let g:ale_fixers = {
			\ '*': ['remove_trailing_lines', 'trim_whitespace'] }
let g:ale_fixers_on_save = 1

let g:fzf_action = {
			\ 'ctrl-t': 'tab split',
			\ 'ctrl-j': 'split',
			\ 'ctrl-l': 'vsplit' }

let g:NERDTreeRespectWildIgnore=1

let g:OmniSharp_server_stdio = 1
let g:OmniSharp_selector_ui = 'fzf'
let g:OmniSharp_highlighting = 0

augroup cleaning
	"autocmd BufWritePre * %s/\s\+$//e " Remove trailing whitespace
	"autocmd BufWritePre * %s/\($\n\s*\)\+\%$// " Remove trailing empty lines
augroup END

augroup interface
	autocmd!

	" Automatically close NERDTree if it's the last tab
	autocmd BufEnter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
	autocmd BufEnter * call ncm2#enable_for_buffer()

	autocmd VimResized * wincmd =
augroup END

" Remap <Leader>
" https://www.reddit.com/r/vim/comments/1vdrxg/space_is_a_big_key_what_do_you_map_it_to/cerq68d/
map <Space> <Leader>

nmap <Leader><Enter> :nohlsearch<CR>

map <Leader>n :NERDTreeToggle<CR>

nmap <Leader>f :Files<CR>
nmap <Leader>g :GFiles<CR>
nmap <Leader>G :GFiles?<CR>
nmap <Leader><Tab> :Buffers<CR>
nmap <Leader>l :Lines<CR>
nmap <Leader>s :Rg<Space>