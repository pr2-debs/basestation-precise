#!/usr/bin/env python

import os, sys, pwd

# Set UID for wgtest
# If this runs as root, the test will always succeed
if os.getuid() == 0:
    wguid = pwd.getpwnam('wgtest')[2]
    os.seteuid(wguid)

HWLOG_DIR = '/hwlog'

if not os.path.exists(HWLOG_DIR):
    print >> sys.stderr, "\"/hwlog\" directory does not exist. Run \"sudo mkdir /hwlog\"."
    sys.exit(2)

if not os.access(HWLOG_DIR, os.R_OK) and os.access(HWLOG_DIR, os.W_OK) and os.access(HWLOG_DIR, os.X_OK):
    print >> sys.stderr, "\"/hwlog\" directory is not correctly setup. Run \"sudo chmod a+rwx -R /hwlog\""
    sys.exit(2)


HWLOG_FILE = os.path.join(HWLOG_DIR, 'hwlog_check.tmp')
try:
    f = open(HWLOG_FILE, 'w')
    f.write('Hello, world!')
    f.close()
    ok = True
except Exception, e:
    print >> sys.stderr, "Unable to create file in /hwlog. Check directory permissions"
    print >> sys.stderr, "\"/hwlog\" directory is not correctly setup. Run \"sudo chmod a+rwx -R /hwlog\""
    ok = False
finally:
    if os.path.exists(HWLOG_FILE):
        os.remove(HWLOG_FILE)

if ok:
    sys.exit()
else:
    sys.exit(1)
