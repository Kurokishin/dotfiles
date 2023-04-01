# Imports
import os
from typing import List  # noqa: F401
from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from functions import *

# Apps
mod = "mod4"
terminal = guess_terminal()
browser = "librewolf"

# Pywal
colors = []
cache='/home/rafael/.cache/wal/colors'
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append('#ffffff')
    lazy.reload()
load_colors(cache)

# Colors
white = "#ffffff"
black = "#000000"
gray = "#505050"
pink = "#ffc0cb"
purple = "#f3b9ff"

catppuccin_mocha = {
        "rosewater": "#f5e0dc",
        "flamingo": "#f2cdcd",
        "pink": "#f5c2e7",
        "mauve": "#cba6f7",
        "red": "#f38ba8",
        "maroon": "#eba0ac",
        "peach": "#fab387",
        "yellow": "#f9e2af",
        "green": "#a6e3a1",
        "teal": "#94e2d5",
        "sky": "#89dceb",
        "sapphire": "#74c7ec",
        "blue": "#89b4fa",
        "lavender": "#b4befe",
        "text": "#cdd6f4",
        "subtext1": "#bac2de",
        "subtext0": "#a6adc8",
        "overlay2": "#9399b2",
        "overlay1": "#7f849c",
        "overlay0": "#6c7086",
        "surface2": "#585b70",
        "surface1": "#45475a",
        "surface0": "#313244",
        "base": "#1e1e2e",
        "mantle": "#181825",
        "crust": "#11111b",
}

keys = [
    # Switch between monitors
    Key([mod], "i", lazy.to_screen(0)),
    Key([mod], "u", lazy.to_screen(1)),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        
    # Keybindings for resizing windows in MonadTall layout
    Key([mod, "control"], "k", lazy.layout.grow()),
    Key([mod, "control"], "j", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod, "shift"], "k", move_window("k"), desc="Move floating window up"),
    Key([mod, "shift"], "j", move_window("j"), desc="Move floating window down"),
    Key([mod, "shift"], "h", move_window("h"), desc="Move floating window left"),
    Key([mod, "shift"], "l", move_window("l"), desc="Move floating window right"),
    Key([mod, "control"], "space", lazy.window.toggle_floating(), desc="Toggle floating mode"),
    Key([mod, "control"], "c", toggle_floating(center=True), desc="Toggle floating and center"),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Audio control (run 'xev' to know the name of a key)
    Key([mod, "control"], "KP_Add", lazy.spawn("amixer -- sset Master 5%+"), desc="Increase the volume"),
    Key([mod, "control"], "KP_Subtract", lazy.spawn("amixer -- sset Master 5%-"), desc="Decrease the volume"),
    Key([mod, "control"], "KP_Multiply", lazy.spawn("amixer -- sset Master 10%"), desc="Set the volume to a value"),

    # Multimedia keys
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -- sset Master 5%+"), desc="Increase the volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -- sset Master 5%-"), desc="Decrease the volume"),
    Key([], "XF86AudioMute", lazy.spawn("amixer -- sset Master toggle"), desc="Mute speakers"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause player"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to previous"),

    # Custom keybindings
    Key([mod, "control"], "y", lazy.spawn(terminal + " -e ytfzf -s"), desc="Spawn youtube on the terminal"),
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Take screenshot of the selected area"),
	Key([mod], "z", lazy.hide_show_bar(), desc="Toggle the bar"),

    # Control blue light 
    KeyChord([mod, "control"], "b", [
        Key([], "d", lazy.spawn("redshift -P -O 6500"), desc="Average blue light amount"),
        Key([], "n", lazy.spawn("redshift -P -O 3000"), desc="Reduced blue light")
    ]),

    #dmenu integration
    Key([mod], "d", lazy.run_extension(extension.DmenuRun(
        dmenu_prompt=">",
        font="JetBrains Mono",
        fontsize=12,
        foreground=colors[1],
        selected_foreground=black,
        selected_background=colors[1],
    ))),    

    Key([mod, "control"], "x", lazy.run_extension(extension.CommandSet(
        commands= {
            'suspend': 'systemctl suspend',
            'hibernate' : 'systemctl hibernate',
            'reboot': 'systemctl reboot',
            'shutdown': 'systemctl poweroff',
        },
        selected_foreground=black,
        selected_background=colors[1],
    ))),
]

#groups = [Group(i) for i in "123456789"]
groups = [
    Group("1", label=""),
    Group("2", label="II"),
    Group("3", label="III"),
    Group("4", label="IV"),
    Group("5", label="", matches=[Match(wm_class=["microsoft teams - preview"])]),
    Group("6", label="VI"),
    Group("7", label="VII"),
    Group("8", label="", matches=[Match(wm_class=["mpv"])]),
    Group("9", label="", matches=[Match(wm_class=["discord"])])
]

for i in groups:
    keys.extend(
        [
            # mod4 + letter of group = switch to group
            Key(
                [mod], i.name, lazy.group[i.name].toscreen(), desc=f"Switch to group {i.name}",
            ),

            # mod4 + control + letter of group = switch to & move focused window to group
            Key(
                [mod, "control"], i.name, lazy.window.togroup(i.name, switch_group=True), desc=f"Switch to & move focused window to group {i.name}",
            ),

            # mod4 + shift + letter of group = move focused window to group
            Key(
                [mod, "shift"], i.name, lazy.window.togroup(i.name), desc=f"move focused window to group {i.name}",
            ),
        ]
    )

layouts = [                     
    layout.Columns(
        border_focus=colors[4],
        border_normal=colors[0],
        border_focus_stack=colors[1],
        border_normal_stack=gray,
        border_width=2,
        grow_amount=4,
        border_on_single=True,
        insert_position=1
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
#     layout.Stack(num_stacks=2),
#     layout.Bsp(),
#     layout.Matrix(),
#    layout.MonadTall(
#        border_focus=white,
#        border_normal=gray,
#        border_focus_stack=purple,
#        border_normal_stack="#614a66",
#        border_width=2,
#        grow_amount=4,
#        border_on_single=True,
#        insert_position=1
#    ),
#     layout.MonadWide(),
#     layout.RatioTile(),
#     layout.Tile(),
#     layout.TreeTab(),
#     layout.VerticalTile(),
#     layout.Zoomy(),
]

widget_defaults = dict(
    font="Hack Nerd Font Bold",
    fontsize=12,
    padding=6,
    foreground=catppuccin_mocha["text"],
    background=catppuccin_mocha["crust"],
)
extension_defaults = widget_defaults.copy()

clock = widget.Clock()
screens = [
    Screen(
        wallpaper = '~/Pictures/wallpapers/computer_guy.jpg',

        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser('~/.config/qtile/icons')]
                ),
                widget.GroupBox(
                    highlight_method='line',
                    highlight_color=catppuccin_mocha["base"],
                    this_current_screen_border=catppuccin_mocha["lavender"],
                    active=catppuccin_mocha["text"],
                    inactive=catppuccin_mocha["overlay0"],
                    disable_drag=True,
                    hide_unused=True
                ),
                widget.Spacer(length=bar.STRETCH),
                widget.Clock(
                        foreground=catppuccin_mocha["peach"],
                        format=' %I:%M %p'
                ),
                widget.Spacer(),
                widget.CPU(
                    foreground=catppuccin_mocha["mauve"],
                    format=format_icon('') + ' {load_percent}%',
                    mouse_callbacks={'Button1': open_htop}
                ),
                widget.ThermalSensor(
                    foreground=catppuccin_mocha["red"],
                    tag_sensor='Tctl',
                    fmt = format_icon('') + ' {}'
                ),
                widget.Volume(
                    foreground=catppuccin_mocha["green"],
                    fmt=format_icon('墳') + ' {}',
                    mouse_callbacks={'Button1': open_pavu}
                ),
                widget.Clock(
                        foreground=catppuccin_mocha["pink"],
                        format=' %m-%d-%Y %a',
                ),
                widget.Systray(
                    padding=3
                ),
            ],
            # Bar height
            20,
            ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

#dgroups_key_binder = None
#dgroups_key_binder = simple_key_binder(mod) 
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = "floating_only" 
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=purple,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

# Configuration variables
auto_fullscreen = False 
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "iG3D"
