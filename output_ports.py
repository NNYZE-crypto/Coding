# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

def port_validation():

	regex = r"(^\d.*)(I.*)"

	test_str = ("Port Summary\n"
		"Port     Display              VLAN Name           Port  Link  Speed  Duplex\n"
		"#        String               (or # VLANs)        State State Actual Actual\n"
		"========================================================================\n"
		"1        IMP_WAN_Transfer     (0002)              E     A     1000   FULL\n"
		"2        IMP-Servers          Server              E     R\n"
		"3        IMP_Mgmt_Vlan_1      Default             E     R\n"
		"4        IMP_Mgmt_Vlan_1      Default             E     R\n"
		"5        IMP-Printers         Printer             E     A     100    FULL\n"
		"6        IMP-Printers         Printer             E     A     100    FULL\n"
		"7        IMP-Printers         Printer             E     R\n"
		"8        IMP-Printers         Printer             E     R\n"
		"9        IMP-Printers         Printer             E     R\n"
		"1: 10    IMP-Printers         Printer             E     R\n"
		"11       IMP-Qos-Client-Port  Clients             E     A     1000   FULL\n"
		"12       IMP-Qos-Client-Port  Clients             E     R\n"
		"13       IMP-Qos-Client-Port  Clients             E     R\n"
		"14       IMP-Qos-Client-Port  Clients             E     R\n"
		"15       IMP-Qos-Client-Port  Clients             E     A     10     FULL\n"
		"16       IMP-Qos-Client-Port  Clients             E     R\n"
		"17       IMP-Qos-Client-Port  Clients             E     R\n"
		"18       IMP-Qos-Client-Port  Clients             E     R\n"
		"19       IMP-Qos-Client-Port  Clients             E     R\n"
		"20       IMP-Qos-Client-Port  Clients             E     R\n"
		"21       IMP-Qos-Client-Port  Clients             E     R\n"
		"22       IMP-Qos-Client-Port  Clients             E     R\n"
		"23       IMP-Qos-Client-Port  Clients             E     R\n"
		"24       IMP-Qos-Client-Port  Clients             E     R\n"
		"25       IMP-Qos-Client-Port  Clients             E     R\n"
		"26       IMP-Qos-Client-Port  Clients             E     R\n"
		"27       IMP-Qos-Client-Port  Clients             E     R\n"
		"28       IMP-Qos-Client-Port  Clients             E     R\n"
		"29       IMP-Qos-Client-Port  Clients             E     R\n"
		"30       IMP-Qos-Client-Port  Clients             E     R\n"
		"31       IMP-Qos-Client-Port  Clients             E     A     100    FULL\n"
		"32       IMP-Qos-Client-Port  Clients             E     R\n"
		"33       IMP-Qos-Client-Port  Clients             E     R\n"
		"34       IMP-Qos-Client-Port  Clients             E     R\n"
		"35       IMP-Qos-Client-Port  Clients             E     R\n"
		"36       IMP-Qos-Client-Port  Clients             E     R\n"
		"37       IMP-Qos-Client-Port  Clients             E     R\n"
		"38       IMP-Qos-Client-Port  Clients             E     R\n"
		"39       IMP-Qos-Client-Port  Clients             E     R\n"
		"40       IMP-Qos-Client-Port  Clients             E     R\n"
		"41       IMP-Qos-Client-Port  Clients             E     R\n"
		"42       IMP-Qos-Client-Port  Clients             E     R\n"
		"43       IMP-Qos-Client-Port  Clients             E     R\n"
		"44       IMP-Qos-Client-Port  Clients             E     R\n"
		"45       IMP-Qos-Client-Port  Clients             E     R\n"
		"46       IMP-Qos-Client-Port  Clients             E     R\n"
		"47       IMPSA0215_P24        (0021)              E     A     1000   FULL\n"
		"48       IMP_Uplink_tag_Ph2   (0021)              E     A     1000   FULL\n"
		"49       IMP_Uplink_tag_Ph2   (0021)              E     R\n"
		"50       IMP_Uplink_tag_Ph2   (0021)              E     R\n"
		"51       IMP_Uplink_tag_Ph2   (0021)              E     R\n"
		"52       IMP_Uplink_tag_Ph2   (0021)              E     R\n"
		"========================================================================\n")

	matches = re.finditer(regex, test_str, re.MULTILINE)
	port = "10-20"
	a = []
	b = {}
	for matchNum, match in enumerate(matches, start=1):
		a.append(match.group(1))
	a = str(a).replace(" ", "")
	print(a)
	if port in a:
	    print("Port Number %s is legit on the switch" % port)
	else:
		print("Port Number %s is not on the switch" % port)

port_validation()
#    for groupNum in range(0, len(match.groups())):
#        groupNum = groupNum + 1
#        ports_available = match.group(1)
    #    print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
