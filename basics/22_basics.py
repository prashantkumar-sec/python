# Standard library: ready-made modules
#
import os, sys, json, datetime, random, math, ipaddress

print(os.getcwd())
print(math.sqrt(16))
print(datetime.datetime.now())

net = ipaddress.ip_network("192.168.1.0/24")
print(net.num_addresses)