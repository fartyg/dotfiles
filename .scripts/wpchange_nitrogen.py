#! /usr/bin/env python3

import os,random
from datetime import datetime

precmd = "DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus"  
cmd = "nitrogen --set-zoom-fill"
wpdir = "/home/aj/Pictures/wp_rotation/"
hour = datetime.now().hour

if hour >= 5 and hour <= 10:
    mood = "morning"

elif hour >= 11 and hour <= 16:
    mood = "day" 

elif hour >= 17:
    mood = "evening" 

else:
    mood = "night"

wp = random.choice(os.listdir(wpdir + mood))
os.system(precmd + " " + cmd + " " + "\"" + wpdir + mood + "/" + wp + "\"")

#except FileNotFoundError:
 #   print("File/directory not found. Make sure wpdir is set correctly.")
