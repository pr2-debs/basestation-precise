#!/usr/bin/env python

outstring =  "# The following assigns all odd robot mac-addresses to 10.68.0.1.\n"
outstring += "# The vast number of entries is due to the fact we only have a byte-level wildcard.\n"
outstring += "# dhcp-mac and dhcp-range are a workaround since the appropriate dhcp-host invocation\n"
outstring += "# exeeds 1024 characters which the parser doesn't seem to like\n\n"

outstring += "dhcp-range=net:c1,10.68.0.1,10.68.0.1,2m\n"
for i in range(1,256,2):
    outstring += "dhcp-mac=c1,00:23:8b:*:*:%.2x\n"%i
for i in range(1,256,2):
    outstring += "dhcp-mac=c1,00:1e:68:*:*:%.2x\n"%i

print outstring
