#! /usr/bin/env python

"""
usage: %(progname)s [args]
"""


import os, sys, string, time, getopt, tempfile

import neo_cgi, neo_util, neo_cs

import subprocess

def sha1_hash(fn):
  p = subprocess.Popen(["sha1sum", "-b", fn], stdout=subprocess.PIPE)
  r,e = p.communicate()
  sha1 = r.split()[0]

  return sha1

def receive(ncgi):
  respository_path = "/hwlogs"

  hdf = ncgi.hdf
  reference = hdf.getValue("Query.reference", "")
  client_hash = hdf.getValue("Query.hash", "")
  filename = hdf.getValue("Query.uploaded", "")

  if not reference: return None

  path = os.path.join(respository_path, reference)
  newpath = os.path.join(path, "new")
  tmppath = os.path.join(path, "tmp")

  fn = os.path.join(newpath, "%s_%s.bag" % (reference, client_hash))
  if os.path.exists(fn):
    return "%s" % (os.stat(fn).st_size, )

  ifp = ncgi.filehandle("uploaded")

  try:  os.makedirs(newpath)
  except os.error, reason:  pass

  try:  os.makedirs(tmppath)
  except os.error, reason:  pass

  ## write the CGI data
  sfp = tempfile.NamedTemporaryFile(dir=tmppath, delete=False)
  sfp.write(ncgi.hdf.writeString())
  sfp.close()

  myhash = hashlib.sha1()

  ## receive the file
  ofp = tempfile.NamedTemporaryFile(dir=tmppath, delete=False)
  while 1:
    buf = ifp.read(8196)
    if not buf: break
    myhash.update(buf)
    ofp.write(buf)
  ofp.close()

  #hash = sha1_hash(ofp.name)
  hash = myhash.digest()

  #now = time.strftime("%Y%m%d-%H%M%S", time.localtime())
  fn = os.path.join(newpath, "%s_%s.bag" % (reference, hash))

  ## move from tmp to new
  os.rename(ofp.name, fn)
  os.rename(sfp.name, fn + ".dat")

  return "%s %s" % (os.stat(fn).st_size, hash)

def main():
  neo_cgi.cgiWrap(sys.stdin, sys.stdout, os.environ)
  neo_cgi.IgnoreEmptyFormVars(1)
  ncgi = neo_cgi.CGI()
  ncgi.parse()

  ret = receive(ncgi)

  print "Content-type: text/plain"
  print
  if ret:
    print "success", ret
  else:
    print "fail"
    

if __name__ == "__main__":
  main()
