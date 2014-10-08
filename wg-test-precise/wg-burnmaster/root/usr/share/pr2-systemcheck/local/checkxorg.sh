#!/bin/bash

res=0

XORG_FILE=/etc/X11/xorg.conf

if [ -e $XORG_FILE ]; then
    nvidia_present=`grep nvidia $XORG_FILE|wc -l`
    if [ $nvidia_present == 0 ]; then
	echo "\"nvidia\" not found in \"/etc/X11/xorg.conf\". Invalid configuration" >&2
	res=2
    fi
else
    echo "File \"/etc/X11/xorg.conf\" does not exist. Graphics will not work. Run \"sudo nvidia-xconfig\" to create this file."
    res=1
fi

exit ${res}