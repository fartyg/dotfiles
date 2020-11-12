# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401
import os, subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen, Match
from libqtile.lazy import lazy
from libqtile.config import ScratchPad, DropDown

mod = 'mod1'
terminal = 'alacritty'
font = 'Noto Sans'
fontsize = 14
music_cmd = ('dbus-send --print-reply --dest=org.mpris.MediaPlayer2.ncspot '
             '/org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.')
# Colors
bgcolor = '262626'
gray = '404040'
anothergray = '606060'
finalgray = '909090'
bordercolor = finalgray
yellow = 'e5c463'
red = 'f85e84'
green = '9ecd6f'
magenta = 'ab9df2'
blue = '7accd7'
cyan = 'ef9062'
white = 'e3e1e4'


keys = [
    # Switch between windows in current stack pane
    Key(
        [mod], 'j',
        lazy.layout.down(),
        desc='Move focus down in stack pane'
    ),
    Key(
        [mod], 'k',
        lazy.layout.up(),
        desc='Move focus up in stack pane'
    ),
    Key(
        [mod], 'h',
        lazy.layout.shrink_main()
    ),
    Key(
        [mod], 'l',
        lazy.layout.grow_main()
    ),
    # Move windows up or down in current stack
    Key(
        [mod, 'control'], 'j',
        lazy.layout.shuffle_down(),
        desc='Move window down in current stack'
    ),
    Key(
        [mod, 'control'], 'k',
        lazy.layout.shuffle_up(),
        desc='Move window up in current stack'
    ),
    Key(
        [mod], "n",
        lazy.layout.normalize()
    ),
    Key(
        [mod], "o",
        lazy.layout.maximize()
    ),
    Key(
        [mod], "g",
        lazy.window.toggle_fullscreen()
    ),
    Key(
        [mod], "p",
        lazy.layout.flip()
    ),
    # Switch window focus to other pane(s) of stack
    Key(
        [mod], 'space',
        lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'
    ),
    # Swap panes of split stack
    Key(
        [mod, 'shift'], 'space',
        lazy.layout.rotate(),
        desc='Swap panes of split stack'
    ),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, 'shift'], 'Return',
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'
    ),
    Key(
        [mod], 'Return',
        lazy.spawn(terminal),
        desc='Launch terminal'
    ),
    Key(
        [mod], 'Tab',
        lazy.next_layout(),
        desc='Toggle between layouts'
    ),
    Key(
        [mod], 'q',
        lazy.window.kill(),
        desc='Kill focused window'
    ),
    Key(
        [mod, 'control'], 'r',
        lazy.restart(),
        desc='Restart qtile'
    ),
    Key(
        [mod, 'control'], 'q',
        lazy.shutdown(),
        desc='Shutdown qtile'
    ),
    Key(
        [mod], 'r',
        lazy.spawncmd(),
        desc='Spawn a command using a prompt widget'
    ),
    Key(
        [], "Print",
        lazy.spawn("scrot -e 'mv $f /home/aj/Pictures/screenshots'"),
        desc='Take a screenshot'
    ),
    Key(
        [mod], 'comma',
        lazy.spawn('/usr/bin/rofi -combi-modi window,drun -show combi -modi combi'),
        desc='Launch rofi'
    ),
    Key(
        [mod], 't',
        lazy.spawn('alacritty -e vifm'),
        desc='Launch vifm'
    ),
    Key(
        [mod], 'm',
        lazy.spawn('thunderbird'),
        desc='Launch thunderbird'
    ),
   Key(
        [mod], 'b',
        lazy.spawn('env MOZ_X11_EGL=1 firefox'),
        desc='Launch firefox'
    )
]

groups = [
    Group('a', spawn=terminal),
    Group('s', layout='monadwide', spawn=terminal),
    Group('d', layout='monadwide', spawn='alacritty -e vifm'),
    Group('f', spawn='env MOZ_X11_EGL=1 firefox'),
    Group('u'),
    Group('i')
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key(
            [mod], i.name,
            lazy.group[i.name].toscreen(),
            desc='Switch to group {}'.format(i.name)
        ),
        # mod1 + shift + letter of group
        # = switch to & move focused window to group
        Key(
            [mod, 'shift'], i.name,
            lazy.window.togroup(i.name, switch_group=True),
            desc='Switch to & move focused window to group {}'.format(i.name)
        ),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, 'shift'], i.name, lazy.window.togroup(i.name),
        #     desc='move focused window to group {}'.format(i.name)),
    ])

groups.append(
    ScratchPad('scratchpad', [
        # define a drop down terminal.
        # it is placed in the upper third of screen by default.
        DropDown(
            'term',
            'alacritty',
            opacity=1,
            height=0.50,
            width=0.60,
            x=0.23,
            y=0.32
        )
    ])
)

keys.extend([
    # Scratchpad
    # toggle visibiliy of above defined DropDown named 'term'
    Key(
        [mod], 'minus',
        lazy.group['scratchpad'].dropdown_toggle('term')
    )
])

layout_theme = {
    'border_width': 2,
    'border_focus': bordercolor,
    'border_normal': bgcolor,
    'single_margin': 0,
    'single_border_width': 0,
    'margin': 8,
    'ratio': 0.6,
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
        'padding': 9,
        'background': bgcolor,
        'highlight_method': 'text'
}
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                     margin_y=3,
                     margin_x=0,
                     borderwidth=0,
                     rounded=False,
                     active = anothergray,
                     inactive = bgcolor,
                     highlight_color = red,
                     this_current_screen_border = yellow,
                     this_screen_border = anothergray,
                     foreground = white,
                     background = bgcolor
                ),
                widget.Prompt(),
                widget.Spacer(),
                widget.CPU(
                    format='{load_percent}%',
                    foreground=white,
                    mouse_callbacks = {
                        'Button1': lambda qtile:
                        qtile.cmd_spawn('alacritty -e htop'),
                        'Button2': lambda qtile:
                        qtile.cmd_spawn('pavucontrol'),
                    }
                ),
                widget.Memory(
                    format='{MemUsed} MB',
                    foreground=white
                ),
                widget.DF(
                    visible_on_warn=False,
                    format='{uf} {m}B',
                    foreground=white
                ),
                widget.Mpris2(
                    foreground=green,
                    name='ncspot',
                    objname='org.mpris.MediaPlayer2.ncspot',
                    display_metadata=['xesam:artist', 'xesam:title'],
                    scroll_chars=None,
                    mouse_callbacks = {
                        'Button1': lambda qtile:
                        qtile.cmd_spawn(music_cmd + 'PlayPause'),
                        'Button2': lambda qtile:
                        qtile.cmd_spawn(music_cmd + 'Previous'),
                        'Button3': lambda qtile:
                        qtile.cmd_spawn(music_cmd + 'Next')
                    },
                    stop_pause_text=''
                ),
                widget.PulseVolume(
                    foreground=blue,
                    mouse_callbacks = {
                        'Button3': lambda qtile:
                        qtile.cmd_spawn('pavucontrol')
                    }
                ),
                widget.Backlight(
                        foreground=yellow,
                        backlight_name='intel_backlight',
                        change_command='brightnessctl s {0}'
                ),
                # widget.Systray(icon_size=18),
                widget.Clock(
                    format='%a %H:%M',
                    foreground = cyan,
                    mouse_callbacks = {
                        'Button1': lambda qtile:
                        qtile.cmd_spawn('alacritty -e calcurse')
                    }
                ),
                widget.QuickExit(
                        foreground=red,
                        default_text='x',
                        countdown_format='{}',
                        fontsize=fontsize
                ),
            ],
            18,
            opacity=1
        ),
    ),
]

# Drag floating layouts.
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

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = 'LG3D'

@hook.subscribe.startup_once
def autostart():
    processes = [
        ['/usr/bin/setxkbmap', '-layout', 'se'],
        ['nitrogen', '--restore'],
        ['/home/aj/.scripts/xbindkeys_startup.sh'],
        ['redshift']
    ]

    for p in processes:
        subprocess.Popen(p)
