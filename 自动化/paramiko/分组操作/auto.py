#因为引入了sys模块，该脚本需要在cmd命令行下面运行并且指定ip地址和设备命令两个文件

import paramiko
import time
import getpass
import sys

username = input("Username: ")
password = getpass.getpass("Password: ")
ip_file = sys.argv[1]
cmd_file = sys.argv[2]   #控制台文件获取

iplist = open(ip_file,'r')
for line in iplist.readlines():
    ip = line.strip()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=username,
                       password=password,look_for_keys=False)
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('已经成功登陆交换机 ' + ip)
    command = ssh_client.invoke_shell()
    cmdlist = open(cmd_file,'r') 
    cmdlist.seek(0)
    for line in cmdlist.readlines():
        each_command = line.strip()
        command.send(each_command + '\n')
        time.sleep(0.5)
    cmdlist.close()
    
    output = command.recv(65535).decode('ASCII')
    print(output)

ssh_client.close()