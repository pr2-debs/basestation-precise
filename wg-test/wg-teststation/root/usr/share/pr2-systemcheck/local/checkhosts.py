#!/usr/bin/env python

import socket
import sys
import subprocess

have_errors = False

# Check hostname
my_hostname = socket.gethostname()

# Check ends with ".willowgarage.com"
if not my_hostname.endswith('.willowgarage.com'):
    print >> sys.stderr, "Hostname \"%s\" does not end with \".willowgarage.com\". Invalid name." % my_hostname
    have_errors = True

# Resolve name
try:
    machine_addr = socket.gethostbyname(my_hostname)
except socket.gaierror:
    print >> sys.stderr, "Hostname %s cannot be resolved to an IP." % my_hostname
    have_errors = True

# Check that localhost, name match
my_fqdn = socket.getfqdn()
if my_fqdn != my_hostname:
    print >> sys.stderr, "FQDN \"%s\" does not match hostname \"%s\"" % (my_fqdn, my_hostname)
    have_errors = True

# Check pingable by name
retcode = subprocess.call('ping -c1 -W1 %s > /dev/null' % my_hostname, shell=True)
if retcode != 0:
    print >> sys.stderr, "Unable to ping localhost by name \"%s\"" % my_hostname
    have_errors = True

# Check pingable by localhost
retcode = subprocess.call('ping -c1 -W1 localhost > /dev/null', shell=True)
if retcode != 0:
    print >> sys.stderr, "Unable to ping localhost by using \"localhost\""
    have_errors = True

if have_errors:
    sys.exit(2)
else:
    sys.exit()
