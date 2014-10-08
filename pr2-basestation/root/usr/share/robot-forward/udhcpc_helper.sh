#!/bin/bash

# We use this to work around the fact that udhcpc does not pass
# client-id through to the script.
client=${HOME}

if [[ -e /etc/robot-forward.conf ]]; then

    # Extract comp_id from the config file
    comp_ip=`sed -nre "s/^${client}\s+(.*)\s+.*$/\1/p" /etc/robot-forward.conf`

    case $1 in
	deconfig)

	    /usr/bin/disable-forward ${client}

	    ;;
	
	
	bound)

	    new_ip_address=${ip}
	    
	    /usr/bin/setup-forward ${client} ${comp_ip} ${new_ip_address}
	    
	    ;;
	
	renew)
	    
	    new_ip_address=${ip}

	    /usr/bin/disable-forward ${client}
	    /usr/bin/setup-forward ${client} ${comp_ip} ${new_ip_address}

	    ;;
	
	nak)
	    
	    ;;
    esac
fi