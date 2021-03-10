#!/bin/sh
i3lock --nofork                 \
    --linecolor=00000000        \
    --ignore-empty-password     \
    --keyhlcolor=ebcb8b00       \
    --bshlcolor=d8dee900        \
    --separatorcolor=00000000   \
    --radius=0			        \
    --indpos="1475:700"		    \
    \
    --insidevercolor=00000000	\
    --insidewrongcolor=00000000 \
    --insidecolor=00000000	    \
    \
    --ringcolor=e59d1700        \
    --ringvercolor=a3be8c00     \
    --ringwrongcolor=bf616a00   \
    \
    --clock			            \
    --timecolor=e3e1e4	        \
    --timestr="%H:%M"	        \
    --time-font="Inter Medium" 	\
    --timesize=80		        \
    --timepos="1425:900"		\
    --timecolor=e3e1e4	        \
    \
    --datecolor=e3e1e4	        \
    --datestr="%A, %d %B"	    \
    --datecolor=e3e1e4	        \
    --date-font="Inter Medium" 	\
    --datesize=60	            \
    --datepos="tx:1000:400"	    \
    \
    --veriftext=""              \
    --wrongtext=""              \
    \
    --indicator                 \
    \
    --image="/home/aj/Pictures/wp_rotation/lock.jpg"
