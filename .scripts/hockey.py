#! /usr/bin/env python

import os, sys
import datetime as dt

player = '/usr/bin/mpv'
p = f'--custom-player {player}'

now = dt.datetime.now()

try:
    inp = int(sys.argv[1])
    date = now + dt.timedelta(inp)

except:
    date = now

d = date.strftime('%Y/%m/%d').replace('/', '')
cmd = f'lazystream --date {d} play select {p}'

os.system(cmd)
