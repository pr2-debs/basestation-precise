#!/bin/sh

. /etc/ros/hydro/setup.sh

if [ $# -eq 0 ] ; then
    /bin/echo "Entering environment at /opt/ros/hydro"
    $SHELL
    /bin/echo "Exiting build environment at /opt/ros/hydro"
else
    exec "$@"
fi



