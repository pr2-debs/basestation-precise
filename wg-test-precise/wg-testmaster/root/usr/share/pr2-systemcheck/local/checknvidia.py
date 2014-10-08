#!/usr/bin/env python

import sys
import subprocess

p = subprocess.Popen('lsmod | grep nvidia', stdout = subprocess.PIPE, shell = True)
o, e = p.communicate()
if not p.returncode == 0:
    print >> sys.stderr, "Kernel module \"nvidia\" not found. It is probably not active"
    sys.exit(1)

users_str = o.split()[-1]
try:
    users = int(users_str)
except Exception, e:
    print >> sys.stderr, "Unable to get number of users for Nvidia kernal module. NVidia module data:\n%s" % o
    sys.exit(1)
    
if users == 0:
    print >> sys.stderr, "NVidia module is not in use. This probably means it is not configure or installed."
    sys.exit(1)

print "NVidia kernel module loaded and in use"
sys.exit(0)
