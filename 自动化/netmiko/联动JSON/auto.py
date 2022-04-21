import netmiko
import json
from netmiko import ConnectHandler

# 存放认证失败的设备信息
switch_with_authentication_issue = []
# 存放网络不通的设备信息
switch_not_reachable = []

with open ('switches.json') as f:
    devices = json.load(f)
    for device in devices:
        try:
            with ConnectHandler(**device['connection']) as conn:
                hostname = device['name']
                print(f'已成功登陆交换机{hostname}')
                output = conn.send_command('display cur | inc sysname')
                print(output)
        
        except netmiko.NetmikoAuthenticationException:
            print(device['name'] + "用户验证失败！")
            switch_with_authentication_issue.append(device['connection']['host'])

        except netmiko.ssh_exception.NetmikoTimeoutException:
            print(device['name'] + "目标不可达！")
            switch_not_reachable.append(device['connection']['host'])

print('\n ====结果输出====')
print('*下列交换机用户验证失败: ')
for i in switch_with_authentication_issue:
    print(f'  {i}')

print('*下列交换机不可达: ')
for i in switch_not_reachable:
    print(f'  {i}')
