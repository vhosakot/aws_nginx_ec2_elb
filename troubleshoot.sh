#!/usr/bin/env bash

# Script to print diagnostic information about the system and to
# try to recover overloaded Nginx web server

if [ -z "$1" ]; then
    echo -e "\n  Tool to troubleshoot overloaded Nginx web server."
    echo -e "\n  Usage: $0 <public IP address of EC2 instance>\n"
    exit
fi

set -euxo pipefail

# Check disk space and delete zipped and old logfiles in /var/log/ to free up disk space
ssh -i nginx-priv-key.pem ubuntu@$1 "sudo df -h &&
                                     sudo du -sh /*/ | sort -h &&
                                     sudo apt-get install -y sysstat &&
                                     sudo iostat &&
                                     sudo find /var/log/ -name *.tgz -exec rm -rf {} \; &&
                                     sudo find /var/log/ -name *.gz -exec rm -rf {} \; &&
                                     sudo find /var/log/ -type f -mtime +90 -delete"

# Check memory usage, process tree and list of all the files opened by processes
ssh -i nginx-priv-key.pem ubuntu@$1 "sudo free && 
                                     sudo vmstat &&
                                     sudo mpstat &&
                                     sudo top -b -n 1 &&
                                     sudo pstree &&
                                     sudo lsof"

# Kill zombie processes
set +e
ssh -i nginx-priv-key.pem ubuntu@$1 "kill $(ps -A -ostat,ppid | awk '/[zZ]/ && !a[$2]++ {print $2}')"
set -e

# Check networking configurations
ssh -i nginx-priv-key.pem ubuntu@$1 "sudo apt-get install -y net-tools &&
                                     sudo netstat -tulnp &&
                                     sudo netstat -r &&
                                     sudo route -n &&
                                     sudo ip route show &&
                                     ip a &&
                                     ifconfig &&
                                     cat /etc/networks &&
                                     cat /etc/netplan/* &&
                                     cat /etc/hosts &&
                                     cat /etc/resolv.conf"

# Capture network traffic using tcpdump on all the interfaces if needed

# Restart Nginx web server
ssh -i nginx-priv-key.pem ubuntu@$1 "sudo systemctl restart nginx &&
                                     sleep 5 &&
                                     sudo systemctl status nginx"

# Remove unwated Ubuntu apt packages to free up disk space
ssh -i nginx-priv-key.pem ubuntu@$1 "sudo apt-get -y autoremove &&
                                     sudo apt-get -y autoclean"

# Check kernel settings
ssh -i nginx-priv-key.pem ubuntu@$1 "sudo sysctl -a"

# Check hardware information
ssh -i nginx-priv-key.pem ubuntu@$1 "sudo lshw &&
                                     sudo lscpu &&
                                     sudo lspci &&
                                     sudo lsblk"
