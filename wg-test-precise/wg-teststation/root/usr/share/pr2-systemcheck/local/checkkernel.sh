#!/bin/bash

KERNELVERSION='2.6.31-10-rt'


if [ `uname -r` != $KERNELVERSION ]; then
    echo Incorrect kernel version. Must be $KERNELVERSION, got `uname -r`. >&2
    echo Check machine package status >&2
    exit 1
fi

echo Kernel version OK: `uname -r`

exit 0