#! /usr/bin/env python3
'''
lazystream helper script
annoying having to always select
yesterday due to timezone differences
'''

import os, sys
import datetime as dt

player = '/usr/bin/mpv'
p = f'--custom-player {player}'

# if you passed an int, thats your date
try:
    d = int(sys.argv[1])

# otherwise, yesterday is the date
except:
    now = dt.datetime.now()
    prevday = now - dt.timedelta(1)
    d = prevday.strftime('%Y/%m/%d').replace('/', '')

cmd = f'lazystream --date {d} play select {p}'
os.system(cmd)
