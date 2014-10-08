#!/bin/bash

if [ ! -e /etc/ros/setup.sh ]; then
    echo "Unable to find ROS bash file \"/etc/ros/setup.sh\"." >&2
    exit 2
fi

if [ ! -e /etc/ros/setup.bash ]; then
    echo "Unable to find ROS bash file \"/etc/ros/setup.bash\"." >&2
    exit 2
fi

. /etc/ros/setup.sh

rosstack find pr2_self_test > /dev/null
if [ ! $? -eq 0 ]; then
    echo "Unable to find \"pr2_self_test\" stack location. Invalid ROS install." >&2
    exit 2
fi

rosstack find wg_hardware_test > /dev/null
if [ ! $? -eq 0 ]; then
    echo "Unable to find \"wg_hardware_test\" stack location. Invalid ROS install." >&2
    exit 2
fi

