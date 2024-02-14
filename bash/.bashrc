#
# ~/.bashrc
#

# Exports
export VISUAL=nvim
export EDITOR="$VISUAL"
export LESS_TERMCAP_mb=$'\e[1;32m'
export LESS_TERMCAP_md=$'\e[1;32m'
export LESS_TERMCAP_me=$'\e[0m'
export LESS_TERMCAP_se=$'\e[0m'
# Pesquisa usando 'less'
#export LESS_TERMCAP_so=$'\e[1;31m'
export LESS_TERMCAP_ue=$'\e[0m'
export LESS_TERMCAP_us=$'\e[1;4;31m'
export PATH="$HOME/.local/bin:$PATH"

# Get word definition
function def() {
	sdcv -n --utf8-output --color "$@" 2>&1 | \
	fold --width=$(tput cols) | \
	less --quit-if-one-screen -RX
}

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias \
    ls='ls --color=auto' \
    sudo='doas' \
    p='doas pacman' \
    anki='anki --no-sandbox' \
    yt='ytfzf' \
    autoremove='./.local/bin/autoremove.sh' \
    #autoremove='doas pacman -Rs $(pacman -Qtdq) && doas pacman -Sc' \
	
# Enable vi mode
set -o vi

# Clear terminal regardless of vi mode
bind -m vi-command 'Control-l: clear-screen'
bind -m vi-insert 'Control-l: clear-screen'

# Import colorscheme from 'wal' asynchronously
# &   # Run the process in the background.
# ( ) # Hide shell job control messages.
# Not supported in the "fish" shell.
#(cat ~/.cache/wal/sequences &)

# Alternative (blocks terminal for 0-3ms)
#cat ~/.cache/wal/sequences

# To add support for TTYs this line can be optionally added.
#source ~/.cache/wal/colors-tty.sh

# Padrão
#PS1='[\u@\h \W]$ '

# Custom bash prompt
PS1='[\[\033[0;35m\]\u\[\033[0;34m\]@\[\033[0;32m\]\h\[\033[0;37m\] \w\[\033[00m\]] '
