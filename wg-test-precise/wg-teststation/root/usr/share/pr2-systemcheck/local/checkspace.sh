#!/bin/sh

space=`df / --total | tail -n1 | awk '{print $5}' | sed -re 's/([0-9]*)\%/\1/'`
boot_space=`df /boot --total | tail -n1 | awk '{print $5}' | sed -re 's/([0-9]*)\%/\1/'`

if [ ${space} -ge 80 ]; then
    echo "Hard disk is ${space}% full" >&2
    exit 1
fi


if [ ${boot_space} -ge 80 ]; then
    echo "Boot partition is ${boot_space}% full" >&2
    exit 1
fi

exit 0