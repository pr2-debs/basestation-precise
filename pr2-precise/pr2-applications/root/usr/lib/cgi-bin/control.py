#!/usr/bin/env python


# enable debugging
import cgi, cgitb
import os
import pexpect
import time
import daemon
cgitb.enable()

import popen2


print "Content-type: text/html"
print

print "RESULT"

form = cgi.FieldStorage()
message = form.getvalue("action", "NO_ACTION")

def run(fun):
    out = ""
    v = popen2.popen4(fun)
    for i in v[0]:
        out = out + i
    return out

def run_as_robot(command):
    run = "su applications -c \"" + command + "\""
    child = pexpect.spawn(run)
    result = child.expect(["ssword:", "(yes/no)?"])
    child.sendline("oppose.Cairo:kid")
    out = ""
    for i in child.readlines():
        out = out + i
    return out

def daemonize(command):
    if os.fork():
        with daemon.DaemonContext():
            run_as_robot(command)
    else:
        return

if (message == "GET_STATE"):
    print "USERS"
    active_user = "(UNKNOWN)"
    dead_users = ""
    message = ""
    for i in run("robot users --no-plist").split("\n"):
        if (i.find("Active User:") != -1):
            active_user = i.split(":")[1].strip()
        if (i.find("Message:") != -1):
            message = i.split(":")[1].strip()
        if (i.find("*") != -1):
            dead_users = dead_users + i[i.find("*") + 1:i.find("(")].strip() + ","

    if (active_user == "applications"):
        print "STATE_VALID"
    elif (active_user == "" or active_user == "None"):
        print "STATE_OFF"
    else:
        print "STATE_IN_USE"
        print "USER:", active_user
        if (message != ""):
            print "MESSAGE:", message #TODO: no newlines!

    print
elif (message == "STOP_ROBOT"):
    print "STOPPING_ROBOT"
    result = run_as_robot("robot claim -f -m 'stopping the robot' ; robot stop -f ; robot release")
    print result
    print "DONE"

elif (message == "START_ROBOT"):
    print "STARTING_APP_MAN"
    print run_as_robot('robot claim -f -m "running applications platform"')
    # daemonize
    daemonize('. /var/ros/applications/setup.sh ; roslaunch --skip-log-check /var/ros/applications/applications.launch 2>&1 | rotatelogs /var/log/pr2-applications/apps-%Y-%m-%d-%H_%M_%S.log 200M')
    # Wait for master to become available
    import socket
    s = socket.socket()
    connect = 0
    # Wait for a maximum of 30 seconds
    while connect < 30:
        try:
            s.connect(('localhost', 11311))
            s.close()
            break
        except:
            time.sleep(1)
            connect += 1
    if connect < 30:
        print run_as_robot('. /var/ros/applications/setup.sh ; /var/ros/applications/wait_for_apps.py')
    else:
        print "Connection to master timed out."
    print "DONE"

else:
#    print "REJECT_COMMAND"
#    print "action = STOP_ROBOT,START_ROBOT,GET_STATE"
    print """
<html>
   <body>
      <form action="/cgi-bin/control.py" method="post">
         <button name="action" value="GET_STATE">Get State</button>
         <button name="action" value="STOP_ROBOT">Stop Robot</button>
         <button name="action" value="START_ROBOT">Start Robot</button>
      </form>
   </body>
</html>
"""
    
