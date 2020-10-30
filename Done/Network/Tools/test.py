## trys to convert spectrum csv into abru connection manager .yml
import csv
import os
import uuid

cwd = os.path.dirname(__file__)
with open(os.path.dirname(__file__) +'\List.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row >= 0 in spamreader:
        hostname = row[0].strip('"')
        netaddr = row[1].strip('"')
        device_location = row[2].strip('"')
        f = open(os.path.dirname(__file__) + "\connections.yml", "a")
        output = """
%s:
  KPX title regexp: '.* %s - GNS.*'
  _is_group: 0
  _protected: 0
  auth fallback: 1
  auth type: userpass
  autoreconnect: ''
  autossh: ''
  cluster: []
  description: Connection with '%s in %s'
  embed: 0
  expect: []
  favourite: 0
  ip: %s
  jump ip: 10.225.0.54
  jump key: /home/ubuntu/Documents/Keys/id_rsa
  jump port: 22
  jump user: m-dehrlich
  local after: []
  local before: []
  local connected: []
  mac: ''
  macros: []
  method: SSH
  name: '%s'
  options: ' -x'
  original_parent: 1f8b601e-e75c-4022-852c-dacc7483e67b
  parent: __PAC__EXPORTED__
  pass: EDDA#beste3
  passphrase: ''
  passphrase user: ''
  port: 22
  prepend command: ''
  proxy ip: ''
  proxy pass: ''
  proxy port: 8080
  proxy user: ''
  public key: ''
  quote command: ''
  remove control chars: ''
  save session logs: ''
  screenshots: ~
  search pass on KPX: 0
  send slow: 0
  send string active: ''
  send string every: 60
  send string intro: 1
  send string txt: ''
  session log pattern: <UUID>_<NAME>_<DATE_Y><DATE_M><DATE_D>_<TIME_H><TIME_M><TIME_S>.txt
  session logs amount: 10
  session logs folder: /home/ubuntu/.config/asbru/session_logs
  startup launch: ''
  startup script: ''
  startup script name: sample1.pl
  terminal options:
    audible bell: ''
    back color: '#000000000000'
    bold color: '#cc62cc62cc62'
    bold color like text: 1
    cursor shape: block
    disable ALT key bindings: ''
    disable CTRL key bindings: ''
    disable SHIFT key bindings: ''
    open in tab: 1
    tab back color: '#000000000000'
    terminal backspace: auto
    terminal character encoding: UTF-8
    terminal font: Monospace 9
    terminal scrollback lines: 5000
    terminal select words: -.:_/
    terminal transparency: 0
    terminal window hsize: 800
    terminal window vsize: 600
    text color: '#cc62cc62cc62'
    timeout command: 40
    timeout connect: 40
    use personal settings: ''
    use tab back color: ''
  title: '%s in %s - GNS'
  use prepend command: ''
  use proxy: 3
  use sudo: ''
  user: m-dehrlich
  variables: []
        """
        f.write(output % (uuid.uuid1(), hostname, hostname, device_location, netaddr, hostname, hostname, device_location))
        print(hostname)
        print(', '.join(row))


# # ---
# 3d53b0c5-4bf0-4e7c-9ed1-421a7e9570d7:
#   KPX title regexp: '.*sdemai10n0001 - GNS.*'
#   _is_group: 0
#   _protected: 0
#   auth fallback: 1
#   auth type: userpass
#   autoreconnect: ''
#   autossh: ''
#   cluster: []
#   description: Connection with 'sdemai10n0001'
#   embed: 0
#   expect: []
#   favourite: 0
#   ip: 172.21.12.1
#   jump ip: 10.225.0.54
#   jump key: /home/ubuntu/Documents/Keys/id_rsa
#   jump port: 22
#   jump user: m-dehrlich
#   local after: []
#   local before: []
#   local connected: []
#   mac: ''
#   macros: []
#   method: SSH
#   name: 'sdemai10n0001 - copy'
#   options: ' -x'
#   original_parent: 1f8b601e-e75c-4022-852c-dacc7483e67b
#   parent: __PAC__EXPORTED__
#   pass: EDDA#beste3
#   passphrase: ''
#   passphrase user: ''
#   port: 22
#   prepend command: ''
#   proxy ip: ''
#   proxy pass: ''
#   proxy port: 8080
#   proxy user: ''
#   public key: ''
#   quote command: ''
#   remove control chars: ''
#   save session logs: ''
#   screenshots: ~
#   search pass on KPX: 0
#   send slow: 0
#   send string active: ''
#   send string every: 60
#   send string intro: 1
#   send string txt: ''
#   session log pattern: <UUID>_<NAME>_<DATE_Y><DATE_M><DATE_D>_<TIME_H><TIME_M><TIME_S>.txt
#   session logs amount: 10
#   session logs folder: /home/ubuntu/.config/asbru/session_logs
#   startup launch: ''
#   startup script: ''
#   startup script name: sample1.pl
#   terminal options:
#     audible bell: ''
#     back color: '#000000000000'
#     bold color: '#cc62cc62cc62'
#     bold color like text: 1
#     command prompt: '[#%\$>]|\:\/\s*$'
#     cursor shape: block
#     disable ALT key bindings: ''
#     disable CTRL key bindings: ''
#     disable SHIFT key bindings: ''
#     open in tab: 1
#     password prompt: "([pP]ass|[pP]ass[wW]or[dt](\\s+for\\s+|\\w+@\\w+)*|[cC]ontrase.a|Enter passphrase for key '.+')\\s*:\\s*$"
#     tab back color: '#000000000000'
#     terminal backspace: auto
#     terminal character encoding: UTF-8
#     terminal font: Monospace 9
#     terminal scrollback lines: 5000
#     terminal select words: -.:_/
#     terminal transparency: 0
#     terminal window hsize: 800
#     terminal window vsize: 600
#     text color: '#cc62cc62cc62'
#     timeout command: 40
#     timeout connect: 40
#     use personal settings: ''
#     use tab back color: ''
#     username prompt: '([lL]ogin|[uU]suario|[uU]ser-?[nN]ame|[uU]ser):\s*$'
#   title: 'sdemai10n0001 - GNS'
#   use prepend command: ''
#   use proxy: 3
#   use sudo: ''
#   user: m-dehrlich
#   variables: []
