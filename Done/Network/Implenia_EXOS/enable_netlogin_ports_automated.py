# OS: Extreme EXOS
# Creator: Dominique Ehrlich
# Last Updated: 31.07.2020
# Description: This script will automatically read the current vlan portconfiguration and
#              enable NETLOGIN (MAC, DOT1X) for all ports except Server, WAN-Transfer and
#              Uplinks as well as Server-ILO
#

import os
import re

#command = 'sh ports no-refresh | exclude "(0021)|WAN-Transfer|Server"'
regex = r"(^\d+\:\d+)|(^\d+)"
# cli_out = """Port Summary
# Port     Display              VLAN Name           Port  Link  Speed  Duplex
# #        String               (or # VLANs)        State State Actual Actual
# ========================================================================
# 1:1        IMP-Qos-Client-Port  Clients             E     R
# 2        IMP-Qos-Client-Port  Clients             E     R
# 3        IMP-Qos-Client-Port  Clients             E     R
# 4        IMP-Qos-Client-Port  Clients             E     R
# 5        IMP-Qos-Client-Port  Clients             E     R
# 6        IMP-Qos-Client-Port  Clients             E     R
# 7        IMP-Qos-Client-Port  Clients             E     R
# 8        IMP-Qos-Client-Port  Clients             E     R
# 9        IMP-Qos-Client-Port  Clients             E     R
# 10       IMP-Qos-Client-Port  Clients             E     R
# 11       IMP-Qos-Client-Port  Clients             E     A     1000   FULL
# 12       IMP-Qos-Client-Port  Clients             E     R
# 13       IMP-Qos-Client-Port  Clients             D     R
# 14       IMP-Qos-Client-Port  Clients             E     R
# 15       IMP-Qos-Client-Port  Clients             E     R
# 16       IMP-Qos-Client-Port  Clients             E     R
# 17       IMP-Qos-Client-Port  Clients             E     R
# 18       IMP-Qos-Client-Port  Clients             E     R
# 19       IMP-Qos-Client-Port  Clients             E     R
# 20       IMP-Qos-Client-Port  Clients             E     R
# 21       IMP-Qos-Client-Port  Clients             E     R
# 22       IMP-Qos-Client-Port  Clients             E     R
# 23       IMP-Qos-Client-Port  Clients             E     R
# 24       IMP-Qos-Client-Port  Clients             E     R
# 25       IMP-Qos-Client-Port  Clients             E     R
# 26       IMP-Qos-Client-Port  Clients             E     R
# 27       IMP-Qos-Client-Port  Clients             E     R
# 28       IMP-Qos-Client-Port  Clients             E     R
# 29       IMP-Qos-Client-Port  Clients             E     R                   """

cli_out = exsh.clicmd('sh ports no-refresh | exclude "(0021)|WAN-Transfer|Server|IMP_Mgmt_Vlan_1|WAN_Transfer"', True)
print(cli_out)
for line in cli_out.split('\n'):
    matches = re.finditer(regex, line, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        port = match.group(0)
        print(exsh.clicmd("enable netlogin ports %s dot1x" %port, True))
        print(exsh.clicmd("enable netlogin ports %s mac" %port, True))
        print(exsh.clicmd('create log message "netlogin enabled for %s"' %port, True))
