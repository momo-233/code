
import paramiko
import time

ip = "192.168.11.12"
username = "Mochine"
password = "child233"

#连接套路
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip, username=username,  \
                   password=password,allow_agent=False,look_for_keys=False)
print("Successfully connected to ",ip)

#华为设备命令
command = ssh_client.invoke_shell()
command.send("sys\n")
command.send("interface LoopBack 0\n")
command.send("ip address 1.1.1.1 255.255.255.255\n")
command.send("return\n")
command.send("save\n")
command.send("y\n")

#初次保存需要 command.send("1.cfg\n")

time.sleep(3)
command.send("display this\n")
time.sleep(1)

output = command.recv(65535)
print(output.decode("ascii"))

ssh_client.close()