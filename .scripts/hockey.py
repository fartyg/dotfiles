#! /usr/bin/env python
import os, sys
import datetime as dt

now = dt.datetime.now()

try:
    inp = int(sys.argv[1])
    delta = dt.timedelta(inp)

except:
    delta = dt.timedelta(-1)

# normal default annoying due to TZ diff
# new default is yesterday
date = now + delta

d = date.strftime('%Y%m%d')
p = '--custom-player /usr/bin/mpv'

cmd = f'lazystream --date {d} play select {p}'
os.system(cmd)
