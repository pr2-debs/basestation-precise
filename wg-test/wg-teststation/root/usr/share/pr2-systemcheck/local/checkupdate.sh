#!/bin/bash

if [ `id -u` != 0 ]; then
    echo "This update check must be run as root!"
    exit 254
fi

# Need to make sure this package is installed!
dpkg -l| grep wg-teststation > /dev/null
if [ ${?} != 0 ]; then
    echo "wg-teststation package is not installed!" >&2
    echo "Run \"sudo apt-get install wg-teststation\" to install" >&2
    exit 2
fi

UPDATEFILE=`mktemp -t checkupdate.XXXXXXXXXX`
res=0

apt-get update -qq > /dev/null
apt-get dist-upgrade -s -qq > $UPDATEFILE

grep wg-teststation $UPDATEFILE > /dev/null
if [ ${?} -eq 0 ]; then
    echo "wg-teststation package needs updating." >&2
    echo "Run \"sudo apt-get install wg-teststation\" to update" >&2
    res=2
fi

rm $UPDATEFILE

if [ ${res} -eq 0 ]; then
    echo "wg-teststation package is installed and up-to-date"
fi

exit ${res}