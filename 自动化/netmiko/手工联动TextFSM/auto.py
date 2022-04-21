from netmiko import ConnectHandler
from textfsm import TextFSM

connection_info = {'device_type':'huawei',
      'ip':'192.168.11.11',
      'username':'mochine',
      'password':'child233'}

with ConnectHandler(**connection_info) as conn:
    output = conn.send_command("display vlan")
print(output)
print(type(output))

with open('display.template') as f:
    template = TextFSM(f)
    demo_output = template.ParseText(output)
print(demo_output)

for each in demo_output:
    print(each[0],each[-1])