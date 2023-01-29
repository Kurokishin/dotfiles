from libqtile.lazy import lazy

@lazy.function
def move_window(qtile, direction, x_step=32, y_step=32):
    layout = qtile.current_layout
    window = qtile.current_window
    if window.floating:
        match direction:
            case "k":
                window.cmd_set_position_floating(window.x, window.y - y_step)
            case "j":
                window.cmd_set_position_floating(window.x, window.y + y_step)
            case "h":
                window.cmd_set_position_floating(window.x - x_step, window.y)
            case "l":
                window.cmd_set_position_floating(window.x + x_step, window.y)
    else:
        match direction:
            case "k":
                layout.cmd_shuffle_up()
            case "j":
                layout.cmd_shuffle_down()
            case "h":
                layout.cmd_shuffle_left()
            case "l":
                layout.cmd_shuffle_right()

@lazy.function
def toggle_floating(qtile, center=False, resolution=(1920, 1080), scale=0.8):
    window = qtile.current_window
    if center:
        if not window.floating:
            window.toggle_floating()
        window.cmd_set_size_floating(
            int(resolution[0] * scale), int(resolution[1] * scale)
        )
        window.cmd_center()
        # bar height + margin + border
        window.cmd_set_position_floating(window.x, window.y + (40 + 10 + 10) // 2)
    else:
        window.toggle_floating()

@lazy.function
def open_pavu(qtile):
    qtile.cmd_spawn("pavucontrol")

def format_icon(icon):
    return '<span font="Font Awesome 6 Free Regular">{}</span>'.format(icon)
