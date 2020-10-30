import re

def set_descr(port, descr):
	exsh.clicmd('configure ports {} display-string "{}"'.format(port, descr), True)
#	print descr
#output = exsh.clicmd('sh configuration netlogin', True)
#regex = r'enable netlogin ports (\d:)?(\d\d) ([\w-]+)'

output = exsh.clicmd('sh policy rule port', True)		#PortStr ist local Port und aPID muss mit naechstem Output abgeglichen werten
regex = r'admn\|Port +\|[\w:]+ +\| *\d+\|((?:\d:)?\d+) +\|.*\|.*\|.*\| *(\d+)\|.*\|'
port_pid = re.findall(regex, output, re.MULTILINE)

output = exsh.clicmd('sh policy profile', True)			#Abgleich mit oberen Output und Description ist "Name"
regex = r'\|(\d+) *\|([\w-]+) *\|\w *\|\d+ *\|none *\|.*\|.*\|.*\|[ Y]{3}\|.*\|(?:InUse)? *\|.*\|\d*.*\|'
pid_descr = re.findall(regex, output, re.MULTILINE)

dhcp_snooping = {'IMP_Uplink_tag_Ph2': 	'configure trusted-ports %s trust-for dhcp-server',
			'IMP_WAN_Transfer': 	'configure trusted-ports %s trust-for dhcp-server',
      'IMP-Servers': 	'configure trusted-ports %s trust-for dhcp-server',
}

commands_dhcp_snooping = ['enable ip-security dhcp-snooping vlan ARGE-Clients ports all violation-action drop-packet',
'enable ip-security dhcp-snooping vlan ARGE-DMZ ports all violation-action drop-packet',
'enable ip-security dhcp-snooping vlan Bilfinger-Clients ports all violation-action drop-packet',
'enable ip-security dhcp-snooping vlan Clients ports all violation-action drop-packet snmp-trap',
'enable ip-security dhcp-snooping vlan Default ports all violation-action drop-packet snmp-trap',
'enable ip-security dhcp-snooping vlan IMP-Spec-Serv ports all violation-action drop-packet snmp-trap',
'enable ip-security dhcp-snooping vlan PERI-DSL ports all violation-action drop-packet',
'enable ip-security dhcp-snooping vlan Printer ports all violation-action drop-packet snmp-trap',
'enable ip-security dhcp-snooping vlan Server ports all violation-action drop-packet snmp-trap',
'enable ip-security dhcp-snooping vlan Server-iLo ports all violation-action drop-packet',
'enable ip-security dhcp-snooping vlan TETRAG-I-Vl149 ports all violation-action drop-packet',
'enable ip-security dhcp-snooping vlan TETRAG-II-Vl148 ports all violation-action drop-packet',
'enable ip-security dhcp-snooping vlan Voice-Ph1Vl130 ports all violation-action drop-packet',
'enable ip-security dhcp-snooping vlan WAH-FTTH-Public ports all violation-action drop-packet',
'enable ip-security dhcp-snooping vlan WAH-GIT ports all violation-action drop-packet',
'enable ip-security dhcp-snooping vlan WAN-Transfer ports all violation-action drop-packet snmp-trap',
'enable ip-security dhcp-snooping vlan Wifi-Ph1-VoicePh2 ports all violation-action drop-packet',
'enable ip-security dhcp-snooping vlan Wifi-Ph2Vl250 ports all violation-action drop-packet',
'enable ip-security dhcp-snooping vlan ZZZ-Client ports all violation-action drop-packet',
'enable ip-security dhcp-snooping vlan ZZZ-Server ports all violation-action drop-packet',
'enable ip-security dhcp-snooping vlan ZZZ-Server-iLo ports all violation-action drop-packet']

exsh.clicmd('disable snmp traps port-up-down ports all', True)

for c in commands_dhcp_snooping:
	exsh.clicmd(c)

for i in port_pid:
	port, pid = i
	pid, descr = [x for x in pid_descr if x[0] == pid][0]
	if descr == 'IMP_WAN_Transfer':
		wan_port = port
	else:
		wan_port = 0
	set_descr(port, descr)
	if descr in dhcp_snooping:
        exsh.clicmd(dhcp_snooping[descr] % port)
	if descr == 'IMP_AccessPoints':
		exsh.clicmd('enable snmp traps port-up-down ports %s' % port, True)
output = exsh.clicmd('sh netlogin session', True)		#Auth Status: success nehmen & Policy Name als Description
regex = r'Port +: ((?:\d:)?\d+).*\sAuth status +: (success) .*\s.*\s.*\sPolicy index +: \d+ +Policy name +: ([\w\- ()]+)\ '
for i in re.finditer(regex, output, re.MULTILINE):
	port, success, descr = i.groups()
	set_descr(port, descr) #if success is "success" else None

output = exsh.clicmd('sh lldp neighbors', True)			#Port ist local Port & Description Name ist Neighbor + Neighbor Port
regex = r'((?:\d:)?\d+) +((?:\w\w:){5}\w\w) +(.*\S) +(\d+) +(\d+) +(.+)'
for i in re.finditer(regex, output, re.MULTILINE):
	port, neighbor_mac, neighbor_port, ttl, age, neighbor_hostname = i.groups()
	if wan_port is 0:
		if not port == wan_port and not any(map(neighbor_hostname.startswith, ['IMPAP', 'IMPSW', 'IMPSA', 'IMPSC', 'IMPS', 'X4'])):
			continue
		descr = neighbor_hostname + '_' + 'P' + neighbor_port
		set_descr(port, descr)
		print(neighbor_hostname)
		if neighbor_hostname.startswith('IMPAP'):
			exsh.clicmd('enable snmp traps port-up-down ports %s' % port, True)
		if neighbor_hostname.startswith('IMPS'):
			exsh.clicmd('configure trusted-ports %s trust-for dhcp-server' % port, True)
	else:
		if not any(map(neighbor_hostname.startswith, ['IMPAP', 'IMPSW', 'IMPSA', 'IMPSC', 'IMPS', 'X4'])):
			continue
		descr = neighbor_hostname + '_' + 'P' + neighbor_port
		set_descr(port, descr)
