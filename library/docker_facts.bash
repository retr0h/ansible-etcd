#!/usr/bin/env bash

IP=$(/sbin/ip route|awk '/eth0.*scope/ { print $9 }')

cat <<EOF
{
    "ansible_facts": {
        "ansible_eth0": {
            "device": "eth0",
            "ipv4": {
                "address": "${IP}"
            }
        }
    }
}
EOF
