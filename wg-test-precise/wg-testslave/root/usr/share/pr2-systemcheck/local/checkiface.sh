#!/bin/bash

res=0

IFCONFIG_FILE=`mktemp -t checkiface.XXXXXXXXX`

ifconfig -s > $IFCONFIG_FILE

for iface in ecat0 lo wan0; do
    grep ${iface} $IFCONFIG_FILE > /dev/null
    if [ ! ${?} -eq 0 ]; then
	echo "${iface} is not up" >&2
	res=2
    else
	echo "${iface} is up, OK"
    fi
done



rm $IFCONFIG_FILE

exit ${res}