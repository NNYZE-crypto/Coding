import re

regex = r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}|(^VLAN\ \d+)|(.*Primary IP:.*)|(Ports:.*)|(.*Untag:.*)"

test_str = ("10.192.16.1\n"
	"VLAN 130: sh vlan Voice-Ph1Vl130\n"
	"    Primary IP:		 10.192.23.1/24\n"
	"    Ports:   28. 	  (Number of active ports=8)\n"
	"       Untag: *27(IMP-QoS-Voice-Ports)m,28(IMP-QoS-Voice-Ports)m\n"
	"VLAN 140: sh vlan ARGE-DMZ\n"
	"    Ports:   26. 	  (Number of active ports=7)\n"
	"VLAN 160: sh vlan ARGE-Clients\n"
	"    Ports:   29. 	  (Number of active ports=9)\n"
	"##################################################\n"
	"10.192.40.1\n"
	"VLAN 130: sh vlan Voice-Ph1Vl130\n"
	"    Ports:   5. 	  (Number of active ports=1)\n"
	"VLAN 140: sh vlan ARGE-DMZ\n"
	"    Ports:   5. 	  (Number of active ports=1)\n"
	"VLAN 160: sh vlan ARGE-Clients\n"
	"    Ports:   6. 	  (Number of active ports=2)\n"
	"##################################################")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):

z    ip = match.matchNum[].groupz
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
