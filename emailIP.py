#!/usr/bin/python

import requests

import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

print get_ip_address('lo')
address = get_ip_address('eth0')
r = requests.post("https://maker.ifttt.com/trigger/rpi_on/with/key/cmCw6R94GQvS-NRLalPZN-", data ={"value1": address})
