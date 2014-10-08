#! /usr/bin/env python

"""
usage: %(progname)s reference filename
"""


import os, sys, string, time, getopt, re, subprocess

import urllib2_file
import urllib2

def sha1_hash(fn): 
  p = subprocess.Popen(["sha1sum", "-b", fn], stdout=subprocess.PIPE) 
  r,e = p.communicate() 
  sha1 = r.split()[0] 
 
  return sha1 

class Sender:
  def __init__(self, site):
    self.site = site
    self.theURL = "http://" + self.site + "/receive"

  def send(self, reference, filename):
    print "sending", reference, filename

    hash = sha1_hash(filename)

    params = {"uploaded" : open(filename)}
    params['reference'] = reference
    params['hash'] = hash
 
    a = urllib2.urlopen(self.theURL + "/" + reference, params)
    response = a.read()

    parts = response.split()
    if len(parts) == 0: 
      print filename, "response:", response
      return False

    if parts[0] != "success": 
      print filename, "response:", response
      return False

    if int(parts[1]) != os.stat(filename).st_size:
      print filename, "file size mismatch", parts[1], os.stat(filename).st_size
      return False

    if len(parts) == 3 and parts[2] != hash: 
      print filename, "hash mismatch", parts[1], hash
      return False

    return True

  def send_dir(self, reference, path):

    donedir = os.path.join(path, "done")
    if not os.path.exists(donedir): os.makedirs(donedir)

    files = os.listdir(path)
    for fn in files:
      ffn = os.path.join(path, fn)
      if not os.path.exists(ffn): continue
      if os.path.isdir(ffn): continue
      
      if self.send(reference, ffn):
        os.rename(ffn, os.path.join(donedir, fn))

def usage(progname):
  print __doc__ % vars()

def main(argv, stdout, environ):
  progname = argv[0]
  optlist, args = getopt.getopt(argv[1:], "", ["help"])

  testflag = 0
  if len(args) == 0:
    usage(progname)
    return
  for (field, val) in optlist:
    if field == "--help":
      usage(progname)
      return

  s = Sender("hwlogs.willowgarage.com")
  #s = Sender("localhost")

  ref = args[0]
  path = args[1]
  s.send_dir(ref, path)


if __name__ == "__main__":
  main(sys.argv, sys.stdout, os.environ)
