from typing import List  # noqa: F401
from libqtile import qtile
import os, subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen, Match
from libqtile.lazy import lazy
from libqtile.config import ScratchPad, DropDown

mod = 'mod1' # alt
terminal = 'alacritty'
browser = ['env', 'MOZ_X11_EGL=1', 'firefox']

fontsize = 13
font = 'Inter'
boldfont = font + ' Semibold'
font += ' Medium'

# sonokai + gray colors
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

activeborder = '52596B' 
inactiveborder = bgcolor
margin = 10

home = os.path.expanduser('~')
music = ('dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify '
        '/org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.')

rofi = '''rofi -combi-modi window,drun -show combi -modi combi \
       -me-select-entry \'\' -me-accept-entry \'MousePrimary\'
       '''

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
    Key([mod], 'e', lazy.layout.previous()),
    Key([mod, 'control'], 'space', lazy.screen.next_group()),
    Key([mod], 'Return', lazy.spawn(terminal)),
    Key([mod], 'r', lazy.spawncmd()),
    Key([mod], 'Tab', lazy.next_layout()),
    Key([mod], 'q', lazy.window.kill()),
    Key([mod], 'odiaeresis', lazy.spawn('thunderbird')), # thunderbörd
    Key([mod], 'b', lazy.spawn(browser)),
    Key([mod, 'control'], 'r', lazy.restart()),
    Key([mod, 'control'], 'q', lazy.spawn(f'{home}/.scripts/power.sh')),
    Key([mod, 'control'], 'l', lazy.spawn(f'{home}/.scripts/lock.sh')),
    Key([mod, 'control'], 'g', lazy.hide_show_bar()),
    Key([mod, 'control'], 'Right', lazy.spawn(music + 'Next')),
    Key([mod, 'control'], 'Left', lazy.spawn(music + 'Previous')),
    Key([], 'Pause', lazy.spawn(music + 'PlayPause')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('pactl set-sink-volume 0 +5%')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('pactl set-sink-volume 0 -5%')),
    Key([], 'XF86AudioMute', lazy.spawn('pactl set-sink-mute 0 toggle')),
    Key([], 'XF86MonBrightnessUp', lazy.spawn('brightnessctl s +100')),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('brightnessctl s 100-')),
    Key([], 'Print', lazy.spawn(['scrot', '-e', f'mv $f {home}/Pictures/screenshots'])),
    Key([], 'Super_L', lazy.spawn(rofi)),
    Key([mod, 'shift'], 'f', lazy.window.toggle_floating()),
    Key([mod, 'shift'], 'b', lazy.window.bring_to_front()),
]

groups = [Group(i) for i in 'asdfui']

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

dropdown_conf = {
    'height': 0.5,
    'opacity': 1,
    'warp_pointer': False
}

groups.append(
    ScratchPad('sp',
        [
            DropDown(
                'term',
                terminal,
                **dropdown_conf
            ),
            DropDown(
                'perfmon',
                [terminal, '-e', 'htop'],
                **dropdown_conf
            ),
            DropDown(
                'filemanager',
                'thunar',
                **dropdown_conf
            ),
            DropDown(
                'rss',
                [terminal, '-e', 'newsboat'],
                **dropdown_conf
            ),
            DropDown(
                'sound',
                'pavucontrol',
                **dropdown_conf
            )
        ]
    )
)

keys.extend([
    Key(
        [], 'VoidSymbol', # unmapped Caps_Lock
        lazy.group['sp'].dropdown_toggle('term')
    ),
    Key(
        [mod], 'e',
        lazy.group['sp'].dropdown_toggle('perfmon')
    ),
    Key(
        [mod], 't',
        lazy.group['sp'].dropdown_toggle('filemanager')
    ),
    Key(
        [mod], 'aring',
        lazy.group['sp'].dropdown_toggle('rss')
    ),
    Key(
        [mod], 'adiaeresis',
        lazy.group['sp'].dropdown_toggle('sound')
    )
])

# for mouse callbacks
# cant call lazy objects with mouse otherwise?
droptoggle = f'{home}/.config/qtile/droptoggle.py'

layout_theme = {
    'border_width': 2,
    'border_focus': activeborder,
    'border_normal': inactiveborder,
    'margin': margin,
    'single_border_width': 0,
    'min_secondary_size': 220,
    'change_ratio': 0.0125,
    'font=': font
}

layouts = [
    layout.MonadWide(
        **layout_theme
    ),
    layout.MonadTall(
        **layout_theme
    )
]

widget_defaults = {
        'font': font,
        'fontsize': fontsize,
        'padding': 10,
        'foreground': yellow,
        'background': bgcolor,
        'highlight_method': 'text'
}
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    fmt='   ❤',
                    foreground=red,
                    mouse_callbacks = {
                        'Button1': lambda qtile:
                        qtile.cmd_spawn(rofi + ' -location 1'),
                        'Button2': lambda qtile:
                        qtile.cmd_spawn([droptoggle, 'term']),
                        'Button3': lambda qtile:
                        qtile.cmd_spawn(f'{home}/.scripts/power.sh')
                    }
                ),
                widget.GroupBox(
                    font=boldfont,
                    fontsize=fontsize+1,
                    borderwidth=0,
                    disable_drag=True,
                    active=anothergray,
                    inactive=bgcolor,
                    this_current_screen_border=yellow,
                    this_screen_border=anothergray,
                    background=bgcolor,
                    urgent_alert_method='text',
                    urgent_text=red
                ),
                widget.Prompt(
                    prompt="run: ",
                    ignore_dups_history=True,
                ),
                widget.Spacer(),
                widget.Mpris2(
                    name='spotify',
                    foreground=green,
                    stop_pause_text='▶',
                    objname='org.mpris.MediaPlayer2.spotify',
                    display_metadata=['xesam:artist', 'xesam:title'],
                    scroll_chars=None,
                    mouse_callbacks = {
                        'Button1': lambda qtile:
                        qtile.cmd_spawn(music + 'PlayPause'),
                        'Button2': lambda qtile:
                        qtile.cmd_spawn(music + 'Previous'),
                        'Button3': lambda qtile:
                        qtile.cmd_spawn(music + 'Next')
                    }
                ),
                widget.Spacer(),
                widget.CPU(
                    format='{load_percent}%',
                    foreground=anothergray,
                    mouse_callbacks = {
                        'Button1': lambda qtile:
                        qtile.cmd_spawn([droptoggle, 'perfmon']),
                        'Button3': lambda qtile:
                        qtile.cmd_spawn(terminal)
                    }
                ),
                widget.Memory(
                    foreground=anothergray,
                    format='{MemUsed} MB'
                ),
                widget.DF(
                    visible_on_warn=False,
                    warn_color=red,
                    warn_space=4,
                    format='{uf} {m}B',
                    foreground=anothergray,
                    mouse_callbacks = {
                        'Button1': lambda qtile:
                        qtile.cmd_spawn([droptoggle, 'filemanager']),
                        'Button2': lambda qtile:
                        qtile.cmd_spawn([terminal, '-e', 'ncdu']),
                        'Button3': lambda qtile:
                        qtile.cmd_spawn([terminal, '-e', 'vifm'])
                    }
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
                    execute=[terminal, '-e', 'yay'],
                    colour_have_updates=orange
                ),
                widget.Clock(
                    font=boldfont,
                    fontsize=fontsize+1,
                    format='%H:%M  ',
                    mouse_callbacks = {
                        'Button1': lambda qtile:
                        qtile.cmd_spawn([droptoggle, 'rss']),
                        'Button2': lambda qtile:
                        qtile.cmd_hide_show_bar(),
                        'Button3': lambda qtile:
                        qtile.cmd_spawn([terminal, '-e', 'calcurse'])
                    }
                )
            ],
            23,
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

@hook.subscribe.client_killed
def fallback(window):
    if window.group.windows != {window}:
        return

    for group in qtile.groups:
        if group.windows:
            qtile.current_screen.toggle_group(group)
            return
    qtile.current_screen.toggle_group(qtile.groups[0])

@hook.subscribe.startup_once
def autostart():
    processes = [
        ['nitrogen', '--restore'],
        ['picom', '--experimental-backends'],
        ['redshift'],
        browser
    ]

    for p in processes:
        subprocess.Popen(p)
