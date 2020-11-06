import os
import re

#masterport = input("Enter the masterport:      ")
#group = input("Enter the ports you want to group. Syntax is either 1 or 1:1 or 1:1-10:      ")
input = 1:1-2,
1:1-3,2:1-3
1:1,1:3
1-4
1,4
input = "1:1-13,2:1-3"
slot = ""
ports = []
x = ""
y = ""
switchtype = "X440-G2-48p"

def split_userinput_stacking(input):
        input = input.split(":")
        slot = str(input[0])
        slot = slot.strip(" ")
        slot = (slot + ":")
        global ports
        ports = str(input[1])
        print("STACKING DETECTED")
        # print(slot)
        return slot, ports

def split_userinput_range(input):
        print(input)
        input = str(input).split(":")
        print(input)
        if ":" in input:
            slot = input[0]
            slot = str(slot)
            range = input[1]
        else:
            range = input[1]
            range = range.split("-")
            print(range)
            x = range[0]
            x = int(x)
            y = range[1]
            print(y)
            y = int(y)
            print(x)
            print(y)
            while x <= y:
                if ":" in input:
                    ports = slot + ":" + str(x)
                    print("execute command for %s" %ports)
                    x = x + 1
                    return ports
                else:
                    print("execute command for %s" %x)
                    x = x + 1

def split_userinput_comma(input):
        input = input.split(",")
        print(input)
        if ":" in input:
            split_userinput_range(input)
        else:
            for i in input:
                print("execute command for port %s" %i)


if ":" in input:
    if "," in input:
        split_userinput_comma(input)
    elif "-" in input:
        split_userinput_range(input)
elif not ":" in input:
    if "-" in input:
        split_userinput_range(input)
    elif "," in input:
        split_userinput_comma(input)
