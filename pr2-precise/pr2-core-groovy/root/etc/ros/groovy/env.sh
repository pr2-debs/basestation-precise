#!/bin/sh

. /etc/ros/groovy/setup.sh

if [ $# -eq 0 ] ; then
    /bin/echo "Entering environment at /opt/ros/groovy"
    $SHELL
    /bin/echo "Exiting build environment at /opt/ros/groovy"
else
    exec "$@"
fi



