#!/bin/bash

# Define the Rofi prompt
prompt="Select an option:"

# Define the options to display in Rofi
options=(
    "Suspend"
    "Hibernate"
    "Reboot"
    "Power Off"
)

# Show the Rofi menu and capture the user's choice
selected=$(printf '%s\n' "${options[@]}" | rofi -dmenu -i -p "$prompt")

# Execute the chosen action
case $selected in
    "Suspend")
        systemctl suspend
        ;;
    "Hibernate")
        systemctl hibernate
        ;;
    "Reboot")
        systemctl reboot
        ;;
    "Power Off")
        systemctl poweroff
        ;;
    *)
        exit 1
        ;;
esac

