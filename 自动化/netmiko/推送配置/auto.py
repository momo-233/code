from netmiko import ConnectHandler

info = {'device_type':'huawei',
        'ip':'192.168.11.11',
        'username':'mochine',
        'password':'child233'}

commands = ['interface GigabitEthernet 0/0/1', 'description descby_send_config_set()']

with ConnectHandler(**info) as connect:
        print ("已经成功登陆交换机" + info['ip'])

        print('===实验目的（1），交互形式推送一条指令。')
        output = connect.send_command('display interface description | include GE0/0/[12][^0-9]')
        print(output)

        print('===实验目的（2），列表形式推送多条指令。')
        output = connect.send_config_set(commands)
        print(output)

        print('===实验目的（3），文件形式推送多条指令。')
        output = connect.send_config_from_file('com.txt')
        print(output)

        print('===最后再检查配置')
        output = connect.send_command('display interface description | include GE0/0/[12][^0-9]')
        print(output)