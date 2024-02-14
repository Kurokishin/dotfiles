#
# ~/.bash_profile
#

# Exports
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_CONFIG_HOME="$HOME/.config"
export XDG_STATE_HOME="$HOME/.local/state"
export XDG_CACHE_HOME="$HOME/.cache"

export LESSHISTFILE=-

export GIT_CONFIG_GLOBAL="$XDG_CONFIG_HOME/git/config"
export CARGO_HOME="$XDG_DATA_HOME"/cargo
export DOCKER_CONFIG="$XDG_CONFIG_HOME"/docker
export GNUPGHOME="$XDG_DATA_HOME"/gnupg
export JUPYTER_CONFIG_DIR="$XDG_CONFIG_HOME"/jupyter
export NPM_CONFIG_USERCONFIG=$XDG_CONFIG_HOME/npm/npmrc
export XINITRC="$XDG_CONFIG_HOME"/X11/xinitrc

[[ -f ~/.bashrc ]] && . ~/.bashrc

# Autostart X at login
if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
	  exec startx
fi
