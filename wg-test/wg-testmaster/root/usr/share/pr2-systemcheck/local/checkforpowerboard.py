#!/usr/bin/env python

# Checks to see if power board is present by listening for UDP packets from
# power board

import os, sys
import subprocess
import tempfile
import time
import signal

if not os.getuid() == 0:
    print >> sys.stderr, "This test must be run as root"
    sys.exit(254)
    
TCP_DUMP_FILE=tempfile.NamedTemporaryFile()


p = subprocess.Popen('tcpdump -i lan0 -c 5 -w %s' % TCP_DUMP_FILE.name,
                     stdout = subprocess.PIPE, stderr = subprocess.PIPE,
                     shell = True)
time.sleep(3)
# Terminate the process if it hasn't finished by now
if p.returncode is not None:
    p.send_signal(signal.SIGINT)

data = TCP_DUMP_FILE.read()

if not 'PR2 Power' in data:
    print >> sys.stderr, "Unable to find PR2 Power board"
    sys.exit(1)

TCP_DUMP_FILE.close()
