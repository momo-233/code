import getpass
import time
import paramiko

username = input("Username:")
password = getpass.getpass("Password:")

#遍历ip地址 从192.168.11.11到192.168.11.16
for i in range(11,16):
    ip = '192.168.11.' + str(i)

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=username,
        password=password,allow_agent=False,look_for_keys=False)
    command = ssh_client.invoke_shell()

    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('已经成功登陆交换机 Layer3Switch-' + str(i-10) + ' ' + ip)
    # 关闭分屏功能
    command.send('screen-length 0 temporary\n')
    # 进入系统视图
    command.send('sys\n')

    for i in range(11,16):
        print('正在创建 VLAN :' + str(i))
        command.send('vlan ' + str(i) + '\n')
        time.sleep(1)
        command.send('desc Python_Vlan' + str(i) + '\n')
        time.sleep(0.5)
    command.send('return\n')
    command.send('save\n')
    command.send('Y\n')
    time.sleep(2)
    output = command.recv(65535).decode('ASCII')
    print(output)

ssh_client.close()