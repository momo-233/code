import re

line = 'Vlanif1          192.168.11.11/24     up         up'
match = re.search('(?P<interface>\S+)\s+(?P<ipaddress>[\w.]+)/', line)
print(match.group('interface'))
print(match.group('ipaddress'))
print(match.group(0))
print(match.groupdict())

all = re.search('(?P<interface>\S+)\s+(?P<ipaddress>[\w.]+)/.*(?P<status>up|down)\s+(?P<protocol>up|down)', line)
print(all.groupdict())