import os
import re
#masterport = input("Enter the masterport:      ")
#group = input("Enter the ports you want to group. Syntax is either 1 or 1:1 or 1:1-10:      ")
masterport = "1:4"
input = "1-100"
switchtype = "x440-G2-24p"
switchtype = "x440-G2-48t"
start_port = ""
end_port = ""

def input_changer():
    slot = input.split(":")
    slot = input[0]
    print(slot)

def port_checker():

    if re.search('\:.*\-', group, re.IGNORECASE): #checks user input if there is a slot and range mentioned
        print("""
        ####################################
        #                                  #
        #  SLOT AND PORT RANGE DETECTED    #
        #                                  #
        ####################################
        """)
        slot = group.split(":")
        slot = (group[0])
        counter = (group[2])
    #    print(group)
        endrange = group.split("-")
        endrange = endrange[1]
        counter = int(counter)
        endrange = int(endrange)
        print(counter)
        print(endrange)
        global start_port
        start_port = str(slot) + ":" + str(counter)
        print(start_port)
        global end_port
        end_port = str(slot) + ":" + str(endrange)
        print(end_port)
        while counter <= endrange:
            print("The current port number is %s:%s" % (slot,counter))
            counter = counter + 1;
        return start_port
        return end_port
    elif re.search('\-', group, re.IGNORECASE): #checks user input if there is a range mentioned
        print("""
        ####################################
        #                                  #
        #           RANGE DETECTED         #
        #                                  #
        ####################################
        """)
        counter = (group[0])
    #    print(group)
        endrange = group.split("-")
        endrange = endrange[1]
        counter = int(counter)
        endrange = int(endrange)
        print(counter)
        print(endrange)
        start_port = []
        while counter <= endrange:
            print("The current port number is %s" % (counter))
            start_port += [counter]
            counter = counter + 1;
        return
    elif re.search('\,', group, re.IGNORECASE): #checks user input if there is a comma seperated
        print("""
        ####################################
        #                                  #
        #    COMMA SEPERATED DETECTED      #
        #                                  #
        ####################################
        """)
        ports = group.split(",")
        for x in ports:
            print("The current port number is %s" % x)
        print(ports)
        start_port = str(ports)
        return start_port
    else:
        print("PFIRSISCH")
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
    		"1:5      IMP-Printers         Printer             E     A     100    FULL\n"
    		"1:6      IMP-Printers         Printer             E     A     100    FULL\n"
    		"1:7      IMP-Printers         Printer             E     R\n"
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
    print(start_port,end_port)
    port = str((start_port, end_port))
    port_comma = str(start_port)
    print("HELLO TEST", port)
    a = []
    b = {}
    for matchNum, match in enumerate(matches, start=1):
    	a.append(match.group(1))
    a = str(a).replace(" ", "")
    print(a)
    if start_port and end_port in a:
        print("Port Range %s is legit on the switch" % (port))
    elif start_port in a:
        print("Port Number %s is legit on the switch" % (start_port))
    elif port_comma in a:
        print("Port Number %s is legit on the switch" % (port_comma))
    else:
        print("LUL")
port_checker()
port_validation()
