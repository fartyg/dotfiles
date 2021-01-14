#! /usr/bin/env python

import os, sys
import datetime as dt

now = dt.datetime.now()

try:
    inp = int(sys.argv[1])
    date = now + dt.timedelta(inp)

except:
    date = now

d = date.strftime('%Y%m%d')
p = '--custom-player /usr/bin/mpv'

cmd = f'lazystream --date {d} play select {p}'
os.system(cmd)
