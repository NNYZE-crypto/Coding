#!/usr/bin/env python

import logging
import re
import sys
import getpass
import paramiko
from paramiko.ssh_exception import AuthenticationException, SSHException
import socket

# logging.basicConfig(level=logging.DEBUG)


client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

HOSTS = [
    "IP",
    # host list from 19FEB;exported by spectrum
]


def fetch_config(host, port, user, password, commands):
    try:
        client.connect(host, port, user, password, timeout=5)
    except (AuthenticationException, SSHException, socket.error) as e:
        out = "Connection failed for host {} reason: {}".format(host, e)
        print out
        return None

    outputs = []
    for command in commands:
        stdin, stdout, stderr = client.exec_command(command)
        outputs.append(stdout.read())
    client.close()
    return outputs


def extract_SysName(show_switch_output):
    match = re.search('^SysName:\s*(.*)$', show_switch_output, re.MULTILINE)
    if match:
        return match.group(1)


def normalize_SysName(sys_name):
    return sys_name.replace('.', '_')


def file_name(filename):
    return filename


def file_path(file_path):
    file_path = '/opt/scripts/output/'
    return file_path


if __name__ == "__main__":
    commands = [
        "sh ports no-refresh | i UPL_IMP",
    ]
    user = raw_input('Enter remote system username: ')
    password = getpass.getpass('Enter remote system password: ')
    # virtualrouter = raw_input('Which VR for File Transfer (mgmt / default):')

    for host in HOSTS:
        outputs = fetch_config(host, 22, user, password, commands)
        filename = "cli_output"
        fileoutput = ""
        if not outputs:
            continue
        if len(outputs) == len(commands):
            for i in range(len(commands)):
                fileoutput += '\n===== Executing {} on {} ==============\n{}'.format(commands[i], host, outputs[i])
                # print outputs
                with open('<FILE>%s.txt' % filename, 'ab') as f:
                    f.write(fileoutput + '\n')
        print "SHOW CONFIG SCRIPT RAN SUCCESSFULL FOR {}".format(host)
