from typing import List  # noqa: F401
import os, subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen, Match
from libqtile.lazy import lazy
from libqtile.config import ScratchPad, DropDown

mod = 'mod1'
terminal = 'alacritty'
font = 'Noto Sans'
fontsize = 16
margin = 14
music_cmd = ('dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify '
             '/org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.')

rofi_cmd = '''/usr/bin/rofi -combi-modi window,drun -show combi -modi combi \
            -me-select-entry \'\' -me-accept-entry \'MousePrimary\'
            '''
rofi_bottom_left = f'{rofi_cmd} -location 7'

# Colors
bgcolor = '2c2e34'
gray = '404040'
anothergray = '808080'
yellow = 'e5c463'
red = 'f85e84'
green = '9ecd6f'
magenta = 'ab9df2'
blue = '7accd7'
orange = 'ef9062'
white = 'e3e1e4'
bordercolor = anothergray

keys = [
    Key([mod], 'j', lazy.layout.down()),
    Key([mod], 'k', lazy.layout.up()),
    Key([mod], 'h', lazy.layout.shrink_main()),
    Key([mod], 'l', lazy.layout.grow_main()),
    Key([mod, 'control'], 'j', lazy.layout.shuffle_down()),
    Key([mod, 'control'], 'k', lazy.layout.shuffle_up()),
    Key([mod], 'n', lazy.layout.normalize()),
    Key([mod], 'm', lazy.layout.maximize()),
    Key([mod], 'comma', lazy.layout.reset()),
    Key([mod], 'g', lazy.window.toggle_fullscreen()),
    Key([mod], 'p', lazy.layout.flip()),
    Key([mod], 'space', lazy.layout.next()),
    Key([mod], 'Return', lazy.spawn(terminal)),
    Key([mod], "r", lazy.spawncmd()),
    Key([mod], 'Tab', lazy.next_layout()),
    Key([mod], 'q', lazy.window.kill()),
    Key([mod], 'aring', lazy.spawn('alacritty -e newsboat')), # båt
    Key([mod], 'adiaeresis', lazy.spawn('pavucontrol')), # pävucontrol
    Key([mod], 'odiaeresis', lazy.spawn('thunderbird')), # thunderbörd
    Key([mod], 't', lazy.spawn('thunar')),
    Key([mod], 'b', lazy.spawn('env MOZ_X11_EGL=1 firefox')),
    Key([mod, 'control'], 'r', lazy.restart()),
    Key([mod, 'control'], 'q', lazy.spawn('/home/aj/.scripts/power.sh')),
    Key([mod, 'control'], 'l', lazy.spawn('/home/aj/.scripts/lock.sh')),
    Key([mod, 'control'], 'g', lazy.hide_show_bar('bottom')),
    Key([mod, 'control'], 'Right', lazy.spawn(music_cmd + 'Next')),
    Key([mod, 'control'], 'Left', lazy.spawn(music_cmd + 'Previous')),
    Key([], 'Pause', lazy.spawn(music_cmd + 'PlayPause')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('pactl set-sink-volume 0 +5%')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('pactl set-sink-volume 0 -5%')),
    Key([], 'XF86AudioMute', lazy.spawn('pactl set-sink-mute 0 toggle')),
    Key([], 'XF86MonBrightnessUp', lazy.spawn('brightnessctl s +100')),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('brightnessctl s 100-')),
    Key([], 'Print', lazy.spawn("scrot -e 'mv $f /home/aj/Pictures/screenshots'")),
    Key([], 'Super_L', lazy.spawn(rofi_bottom_left))
]

groups = [
    Group('a'),
    Group('s'),
    Group('d', layout='monadwide'),
    Group('f'),
    Group('u'),
    Group('i')
]

for i in groups:
    keys.extend([
        Key(
            [mod], i.name,
            lazy.group[i.name].toscreen(),
            desc=f'Switch to group {i.name}'
        ),
        Key(
            [mod, 'control'], i.name,
            lazy.window.togroup(i.name, switch_group=True),
            desc=f'Switch to & move focused window to group {i.name}'
        ),
    ])

groups.append(
    ScratchPad('scratchpad', [
        DropDown(
            'term',
            'alacritty',
            height=0.45,
            opacity=1
        )
    ])
)

keys.extend([
    Key(
        [], 'VoidSymbol', # unmapped Caps_Lock
        lazy.group['scratchpad'].dropdown_toggle('term')
    )
])

layout_theme = {
    'border_width': 2,
    'border_focus': bordercolor,
    'border_normal': bgcolor,
    'margin': margin,
    'single_border_width': 0,
    'min_secondary_size': 220,
    'change_ratio': 0.025,
    'font=': font
}

layouts = [
    layout.MonadTall(
        **layout_theme
    ),
    layout.MonadWide(
        **layout_theme
    )
]

widget_defaults = {
        'font': font,
        'fontsize': fontsize,
        'padding': 8,
        'foreground': yellow,
        'background': bgcolor,
        'highlight_method': 'text'
}
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Image(
                    filename='/home/aj/.config/qtile/arch.png',
                    scale=False,
                    margin_y=4,
                    margin_x=4,
                    mouse_callbacks = {
                        'Button1': lambda qtile:
                        qtile.cmd_spawn(rofi_bottom_left),
                        'Button3': lambda qtile:
                        qtile.cmd_spawn('/home/aj/.scripts/power.sh')
                    }
                ),
                widget.Sep(padding=8, linewidth=0),
                widget.GroupBox(
                    margin_y=4,
                    borderwidth=0,
                    center_aligned=True,
                    rounded=False,
                    disable_drag=True,
                    active=anothergray,
                    inactive=bgcolor,
                    highlight_color=red,
                    this_current_screen_border=yellow,
                    this_screen_border=anothergray,
                    background=bgcolor
                ),
                widget.Prompt(
                    prompt="run: ",
                    ignore_dups_history=True,
                ),
                widget.Spacer(),
                widget.Mpris2(
                    name='spotify',
                    foreground=green,
                    stop_pause_text='',
                    objname='org.mpris.MediaPlayer2.spotify',
                    display_metadata=['xesam:artist', 'xesam:title'],
                    scroll_chars=None,
                    mouse_callbacks = {
                        'Button1': lambda qtile:
                        qtile.cmd_spawn(music_cmd + 'PlayPause'),
                        'Button2': lambda qtile:
                        qtile.cmd_spawn(music_cmd + 'Previous'),
                        'Button3': lambda qtile:
                        qtile.cmd_spawn(music_cmd + 'Next')
                    }
                ),
                widget.Spacer(),
                widget.CPU(
                    format='{load_percent}%',
                    foreground=anothergray,
                    mouse_callbacks = {
                        'Button1': lambda qtile:
                        qtile.cmd_spawn('alacritty -e htop'),
                        'Button2': lambda qtile:
                        qtile.cmd_spawn('pavucontrol')
                    }
                ),
                widget.Memory(
                    foreground=anothergray,
                    format='{MemUsed} MB'
                ),
                widget.DF(
                    visible_on_warn=False,
                    format='{uf} {m}B',
                    foreground=anothergray
                ),
                widget.PulseVolume(foreground=magenta),
                widget.Backlight(
                    foreground=blue,
                    backlight_name='intel_backlight',
                    change_command='brightnessctl s {0}'
                ),
                widget.CheckUpdates(
                    distro='Arch_checkupdates',
                    display_format='{updates}',
                    execute='alacritty -e yay',
                    colour_have_updates=orange
                ),
                widget.Clock(
                    format='%H:%M',
                    mouse_callbacks = {
                        'Button1': lambda qtile:
                        qtile.cmd_spawn('alacritty -e calcurse')
                    }
                )
            ],
            24,
            opacity=1
        ),
    ),
]

mouse = [
    Drag(
        [mod], 'Button1',
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
    ),
    Drag(
        [mod], 'Button3',
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
    Click(
        [mod], 'Button2',
        lazy.window.bring_to_front()
    )
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = 'smart'
floating_layout = layout.Floating(
                     **layout_theme,
                     float_rules=[
                         {'wmclass': 'confirm'},
                         {'wmclass': 'dialog'},
                         {'wmclass': 'download'},
                         {'wmclass': 'error'},
                         {'wmclass': 'file_progress'},
                         {'wmclass': 'notification'},
                         {'wmclass': 'splash'},
                         {'wmclass': 'toolbar'},
                         {'wmclass': 'confirmreset'},  # gitk
                         {'wmclass': 'makebranch'},  # gitk
                         {'wmclass': 'maketag'},  # gitk
                         {'wname': 'branchdialog'},  # gitk
                         {'wname': 'pinentry'},  # GPG key password entry
                         {'wmclass': 'ssh-askpass'},  # ssh-askpass
                     ]
)
wmname = 'LG3D'

@hook.subscribe.startup_once
def autostart():
    processes = [
        ['/usr/bin/setxkbmap', '-layout', 'se', '-option', 'caps:none'],
        ['nitrogen', '--restore'],
        ['picom', '--experimental-backends'],
        ['/home/aj/.scripts/xbindkeys_startup.sh'],
        ['redshift']
    ]

    for p in processes:
        subprocess.Popen(p)
