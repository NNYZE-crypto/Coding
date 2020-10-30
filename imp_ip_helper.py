import re
import os
import sys

print(os.getcwd())
file = open("input.txt")

test_str = file.read()
file.close()

#print(test_str)

matches = ["1.1.1.1"]

device_regex = r'^((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\s*(={50}$\n(?:^[^#]*$\n)*#{50})'
vlan_regex = r'(?:^configure bootprelay vlan (\S+) add ((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))$\n)'

#print("Switch IP","VLAN","IP Helper", sep=',')
for device in re.findall(device_regex, test_str, re.MULTILINE):
    ip = device[0]
    vlan_str = device[1]
    vlans = re.findall(vlan_regex, vlan_str, re.MULTILINE)
    for vlan in vlans:
        if not any(x in vlan[1] for x in matches):
            with open('output.csv', 'a') as f:
                print(ip, vlan[0], vlan[1], sep=',', file=f)
