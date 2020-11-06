import os
import sys
import re

device_regex = r'^((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\s*(={50}$\n(?:^[^#]*$\n)*#{50})'
vlan_regex = r'((VLAN \d+)|(Primary IP:.*\n)|(Ports:.*)|(.*Untag:.*\n))'

file = open("vlan_cleanup.log")

test_str = file.read()
file.close()

#print(test_str)

matches = []

with open("vlan_cleanup.log","r") as fi:
    id = []
    for ln in fi:
        if ln.startswith(("1", "VLAN 130", "VLAN 140", "VLAN 160", "    Primary IP", "    Ports:", "       Untag", "#")):
            #id.append(ln[0:])
            with open('output.log', 'a') as e:
                print(ln, end='',file=e)
print(id)

#print("Switch IP","VLAN","IP Helper", sep=',')
for device in re.findall(device_regex, test_str, re.MULTILINE):
    ip = device[0]
    vlan_str = device[1]
    vlans = re.findall(vlan_regex, vlan_str, re.MULTILINE)
    for vlan in vlans:
        if not any(x in vlan[0] for x in matches):
            with open('output.csv', 'a') as f:
                print(ip, vlan[1], vlan[2], vlan[3], vlsefile 
