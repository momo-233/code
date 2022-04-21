from netmiko import ConnectHandler
from textfsm import TextFSM
from pprint import pprint

connection_info = {'device_type':'huawei',
      'ip':'192.168.11.11',
      'username':'mochine',
      'password':'child233'}

with ConnectHandler(**connection_info) as conn:
    output = conn.send_command("display interface brief",use_textfsm=True)

# print(output)
pprint(output)

