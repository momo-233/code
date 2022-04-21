import netmiko
from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader

allow_ip = ['192.168.11.2', '192.168.11.12']
disallow_ip = ['192.168.11.13', '192.168.11.14']
acl= 2000

sw1 = {'device_type':'huawei',
      'ip':'192.168.11.11',
      'username':'mochine',
      'password':'child233'}

loader = FileSystemLoader('jinja2模板')
environment = Environment(loader=loader)
tpl = environment.get_template('acl.jinja2')
out = tpl.render(allow_ip=allow_ip, disallow_ip=disallow_ip,acl=acl,interface='vty 0 4')

with open("configuration.conf", "w") as f:
       f.write(out)

with ConnectHandler(**sw1) as conn:
        print ("已经成功登陆交换机" + sw1['ip'])
        output = conn.send_config_from_file("configuration.conf")
        print (output)