#! /usr/bin/env python
import datetime as dt
import sys, os

now = dt.datetime.now()

try:
    inp = int(sys.argv[1])
    delta = dt.timedelta(inp)

except:
    delta = dt.timedelta(0)

date = now + delta

d = date.strftime('%Y%m%d')
p = '--custom-player /usr/bin/mpv'

cmd = f'lazystream --date {d} play select {p}'
os.system(cmd)
