#! /usr/bin/env python
import sys
from libqtile.command_client import InteractiveCommandClient
c = InteractiveCommandClient()

w = sys.argv[1]
c.group["sp"].dropdown_toggle(w)
