from libqtile import qtile
import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen, Match
from libqtile.lazy import lazy
from libqtile.config import ScratchPad, DropDown

home = os.path.expanduser('~')
mod = 'mod1'  # alt

fontsize = 13
font = 'Inter'
boldfont = f'{font} Semibold'
font += ' Medium'

# sonokai
bgcolor = '2c2e34'
# altbg = '373a45'
gray = '828282'
yellow = 'e5c463'
red = 'f85e84'
green = '9ecd6f'
magenta = 'ab9df2'
blue = '7accd7'
orange = 'ef9062'
white = 'e3e1e4'

activeborder = gray
inactiveborder = '404040'

margin = 10
barheight = 22
borderwidth = 2

terminal = 'alacritty'
browser = 'env MOZ_X11_EGL=1 firefox'
rofi = ['rofi', '-show']
player_cmd = (
        'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify '
        '/org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.'
)

keys = [
    Key([mod], 'j', lazy.layout.down()),
    Key([mod], 'k', lazy.layout.up()),
    Key([mod], 'h', lazy.layout.shrink_main()),
    Key([mod], 'l', lazy.layout.grow_main()),

    Key([mod, 'control'], 'j', lazy.layout.shuffle_down()),
    Key([mod, 'control'], 'k', lazy.layout.shuffle_up()),

    Key([mod], 'space', lazy.layout.next()),
    Key([mod], 'Tab', lazy.layout.previous()),
    Key([mod], 'Return', lazy.spawn(terminal)),

    Key([mod], 'q', lazy.window.kill()),
    Key([mod], 'n', lazy.layout.normalize()),
    Key([mod], 'm', lazy.layout.maximize()),
    Key([mod], 'comma', lazy.layout.reset()),
    Key([mod], 'g', lazy.window.toggle_fullscreen()),
    Key([mod], 'p', lazy.layout.flip()),

    Key([mod, 'control'], 'r', lazy.restart()),
    Key([mod, 'control'], 'q', lazy.spawn(f'{home}/.scripts/power.sh')),
    Key([mod, 'control'], 'l', lazy.spawn(f'{home}/.scripts/lock.sh')),
    Key([mod, 'control'], 'g', lazy.hide_show_bar()),
    Key([mod, 'control'], 'space', lazy.screen.next_group()),
    Key([mod, 'control'], 'Return', lazy.spawncmd()),
    Key([mod, 'shift'], 'f', lazy.window.toggle_floating()),
    Key([mod, 'shift'], 'b', lazy.window.bring_to_front()),

    Key([mod, 'control'], 'Right', lazy.spawn(f'{player_cmd}Next')),
    Key([mod, 'control'], 'Left', lazy.spawn(f'{player_cmd}Previous')),
    Key([], 'Pause', lazy.spawn(f'{player_cmd}PlayPause')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('pactl set-sink-volume 0 +5%')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('pactl set-sink-volume 0 -5%')),
    Key([], 'XF86AudioMute', lazy.spawn('pactl set-sink-mute 0 toggle')),
    Key([], 'XF86MonBrightnessUp', lazy.spawn('brightnessctl s +100')),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('brightnessctl s 100-')),
    Key([], 'Print', lazy.spawn(
            ['scrot', '-e', f'mv $f {home}/Pictures/screenshots']
        )),
    Key([mod], 'apostrophe', lazy.spawn(
            f'{terminal} -e zsh -c \'. ~/.zshrc; nvim\''
        )),
    Key([], 'Super_L', lazy.spawn(rofi + ['drun'])),
    Key([mod], 'Super_L', lazy.spawn(rofi + ['window'])),
    Key([mod], 'b', lazy.spawn(browser)),
    Key([mod, 'control'], 'b', lazy.spawn(f'{browser} --private-window')),
    Key([mod], 'v', lazy.spawn(f'{terminal} -e amfora')),
    Key([mod], 'odiaeresis', lazy.spawn('thunderbird')),  # thunderbörd
    Key([mod], 'section', lazy.spawn(f'{home}/.scripts/spotify.sh')),
]

groups = [Group(i) for i in 'asdfui']
for i in groups:
    keys.extend(
        [
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
        ]
    )

dropdown_conf = {
    'opacity': 1,
    'warp_pointer': False,
    'height': 0.45,
}

groups.append(
    ScratchPad('sp', [
            DropDown(
                'term',
                terminal,
                **dropdown_conf
            ),
            DropDown(
                'perfmon',
                f'{terminal} -e {home}/.scripts/envfix.sh htop',
                **dropdown_conf
            ),
            DropDown(
                'irc',
                f'{terminal} -e irssi',
                **dropdown_conf
            ),
            DropDown(
                'filemanager',
                'thunar',
                **dropdown_conf
            ),
            DropDown(
                'rss',
                f'{terminal} -e {home}/.scripts/envfix.sh newsboat',
                **dropdown_conf
            ),
            DropDown(
                'sound',
                'pavucontrol',
                **dropdown_conf
            ),
            DropDown(
                'calendar',
                f'{terminal} -e {home}/.scripts/envfix.sh calcurse',
                **dropdown_conf
            )
        ]
    )
)

keys.extend(
    [
        Key(
            [], 'VoidSymbol',  # unmapped Caps_Lock
            lazy.group['sp'].dropdown_toggle('term')
        ),
        Key(
            [mod], 'e',
            lazy.group['sp'].dropdown_toggle('perfmon')
        ),
        Key(
            [mod], 'r',
            lazy.group['sp'].dropdown_toggle('irc')
        ),
        Key(
            [mod], 't',
            lazy.group['sp'].dropdown_toggle('filemanager')
        ),
        Key(
            [mod], 'aring',  # nyhetsbåt
            lazy.group['sp'].dropdown_toggle('rss')
        ),
        Key(
            [mod], 'adiaeresis',  # pävucontrol
            lazy.group['sp'].dropdown_toggle('sound')
        )
    ]
)

layout_theme = {
    'border_width': borderwidth,
    'border_focus': activeborder,
    'border_normal': inactiveborder,
    'margin': margin,
    'ratio': 0.62,
    'single_border_width': 0,
    'min_secondary_size': 220,
    'change_ratio': 0.0075
}
layouts = [layout.MonadTall(**layout_theme)]

widget_defaults = {
        'font': font,
        'fontsize': fontsize,
        'padding': 12,
        'foreground': gray,
        'background': bgcolor,
        'highlight_method': 'text'
}
extension_defaults = widget_defaults.copy()

# for mouse callbacks
# cant call lazy objects with mouse otherwise?
droptoggle = f'{home}/.config/qtile/droptoggle.py'
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    fmt='rofi',
                    font=boldfont,
                    padding=9,
                    fontsize=fontsize-2,
                    mouse_callbacks={
                        'Button1': lambda:
                        qtile.cmd_spawn(rofi + ['drun', '-location', '1']),
                        'Button2': lambda:
                        qtile.cmd_spawn(f'{home}/.scripts/power.sh'),
                        'Button3': lambda:
                        qtile.cmd_spawn(rofi + ['window', '-location', '1']),
                    }
                ),
                widget.GroupBox(
                    font=boldfont,
                    fontsize=fontsize+1,
                    borderwidth=0,
                    disable_drag=True,
                    active=gray,
                    inactive=bgcolor,
                    this_current_screen_border=yellow,
                    this_screen_border=gray,
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
                    stop_pause_text='▶',
                    objname='org.mpris.MediaPlayer2.spotify',
                    display_metadata=['xesam:artist', 'xesam:title'],
                    scroll_chars=None,
                    mouse_callbacks={
                        'Button1': lambda:
                        qtile.cmd_spawn(f'{player_cmd}PlayPause'),
                        'Button2': lambda:
                        qtile.cmd_spawn(f'{player_cmd}Previous'),
                        'Button3': lambda:
                        qtile.cmd_spawn(f'{player_cmd}Next')
                    }
                ),
                widget.Spacer(),
                widget.CPU(
                    format='{load_percent}%',
                    mouse_callbacks={
                        'Button1': lambda:
                        qtile.cmd_spawn(f'{droptoggle} perfmon'),
                        'Button3': lambda:
                        qtile.cmd_spawn(f'{droptoggle} sound')
                    }
                ),
                widget.ThermalSensor(
                        foreground_alert=red,
                        foreground=gray,
                        threshold=85
                ),
                widget.Memory(
                    format='{MemUsed} MB',
                    mouse_callbacks={
                        'Button1': lambda:
                        qtile.cmd_spawn(f'{droptoggle} irc'),
                        'Button3': lambda:
                        qtile.cmd_spawn(f'{droptoggle} term')
                    }
                ),
                widget.DF(
                    visible_on_warn=False,
                    warn_color=red,
                    warn_space=10,
                    format='{uf} {m}B',
                    mouse_callbacks={
                        'Button1': lambda:
                        qtile.cmd_spawn(f'{droptoggle} filemanager'),
                        'Button2': lambda:
                        qtile.cmd_spawn(f'{home}/.scripts/envfix.sh ncdu'),
                        'Button3': lambda:
                        qtile.cmd_spawn(f'{terminal} -e vifm')
                    }
                ),
                widget.PulseVolume(),
                widget.CheckUpdates(
                    distro='Arch_checkupdates',
                    display_format='{updates}',
                    colour_have_updates=orange
                ),
                widget.Clock(
                    font=boldfont,
                    foreground=yellow,
                    fontsize=fontsize+1,
                    format='%H:%M',
                    mouse_callbacks={
                        'Button1': lambda:
                        qtile.cmd_spawn(f'{droptoggle} rss'),
                        'Button2': lambda:
                        qtile.cmd_hide_show_bar(),
                        'Button3': lambda:
                        qtile.cmd_spawn(f'{droptoggle} calendar')
                    }
                )
            ],
            barheight,
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

follow_mouse_focus = False
floating_layout = layout.Floating(
                    **layout_theme,
                    float_rules=[
                        Match(title="Picture-in-Picture"),
                        Match(wm_class="gcolor2"),
                        Match(wm_class="gimp")
                    ]
)


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
        ['picom', '-b', '--experimental-backends'],
        ['redshift'],
        rofi + ['drun']
    ]

    for p in processes:
        subprocess.Popen(p)
