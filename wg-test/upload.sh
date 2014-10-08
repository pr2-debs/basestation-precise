#!/bin/bash
scp $@ rosbuild@pub5:/var/packages/wg-test/ubuntu/queue/lucid/
ssh rosbuild@pub5 reprepro -V -b /var/packages/wg-test/ubuntu processincoming lucid
