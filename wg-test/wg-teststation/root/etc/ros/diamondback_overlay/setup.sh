for var in /etc/ros/diamondback_overlay/env/*[!~]; do
    export ${var##*/}=$(cat ${var})
done

export PATH=${ROS_ROOT}/bin:${PATH}
export PYTHONPATH=${ROS_ROOT}/core/roslib/src