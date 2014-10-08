#!/bin/bash

WGTEST_DIR=/u/wgtest

if [ ! -e $WGTEST_DIR ]; then
    echo "Unable to find home directory wgtest user. NFS may not be up." >&2
    echo "Run \"sudo service autofs restart\" to start NFS" >&2
    exit 2
fi

exit 0