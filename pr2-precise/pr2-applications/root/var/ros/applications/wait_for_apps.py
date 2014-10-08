#!/usr/bin/env python

import rospy

services = [ 'list_apps', 'start_app', 'stop_app', 'install_app',
         'get_app_details', 'uninstall_app', 'list_exchange_apps', ]

def main():
    rospy.init_node('wait_for_apps', anonymous=True)

    # wait for name parameter to be set
    while not rospy.has_param('robot/name'):
        rospy.sleep(0.1)

    name = rospy.get_param('robot/name')
    
    print "Robot name is %s"%(name)

    for s in services:
        service = "%s/%s"%(name, s)
        print "Waiting for service %s"%(service)
        rospy.wait_for_service(service)
        print "Service %s is now available"%(service)

if __name__ == '__main__':
    main()
