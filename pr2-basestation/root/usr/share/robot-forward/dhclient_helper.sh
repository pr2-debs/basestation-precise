#!/bin/bash

if [[ -e /etc/robot-forward.conf ]]; then

    # Extract comp_id from the config file
    comp_ip=`sed -nre "s/^${client}\s+(.*)\s+.*$/\1/p" /etc/robot-forward.conf`

    case ${reason} in
	RELEASE|EXPIRE)

	    /usr/bin/disable-forward ${client}

	    ;;
	
	
	BOUND|REBOOT)

	    /usr/bin/setup-forward ${client} ${comp_ip} ${new_ip_address}
	    
	    ;;
	
	RENEW|REBIND)
	    
	    /usr/bin/disable-forward ${client}
	    /usr/bin/setup-forward ${client} ${comp_ip} ${new_ip_address}

	    ;;
	
	*)
	    
	    ;;
    esac
fi