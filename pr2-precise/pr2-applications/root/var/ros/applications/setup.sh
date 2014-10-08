#!/bin/sh

# Set up the environment, since this will be executed as a daemon
export ROS_MASTER_URI="http://c1:11311"
export ROBOT="pr2"
export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

# export HOSTNAME so that we can use it as the /robot/name parameter
export HOSTNAME=`hostname`
# set our ROS_HOSTNAME to our FQDN, since android doesn't do well with non-fully-qualified domain names
export ROS_HOSTNAME=`hostname -f`

# set ROS_ENV_LOADER to our environment loader
export ROS_ENV_LOADER=/var/ros/applications/env.sh
. /etc/ros/setup.sh
