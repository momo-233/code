import telnetlib
import time

host = '192.168.11.111'
user = 'mochine'
password = 'child233'

tn = telnetlib.Telnet(host)

tn.read_until(b'Username:')
tn.write(user.encode('ascii') + b"\n")
tn.read_until(b"Password:")
tn.write(password.encode('ascii') + b"\n")

tn.write(b'screen-length 0 temporary\n')
# 进入系统视图，配置 Loopback0 口
tn.write(b"sys\n")
tn.write(b"interface LoopBack 0\n")
tn.write(b"ip address 11.11.11.11 255.255.255.255\n")

# 返回用户视图，保存配置
tn.write(b"return\n")
tn.write(b"save\n")
tn.write(b"Y\n")
tn.write(b"1.cfg\n")

# 等待
time.sleep(3)

# 1、打印截屏，此时用 read_very_eager() 能成功,此时不能执行 quit 退出。
# tn.write(b"quit\n") 根据 Python 的文档，quit 后断开 telnet 连接
# 则不能用 read_very_eager 而应该用 read_all,
# 但试了无论quit 不 quit ，都只能用 read_very_eager
tn.write(b"quit\n")
output = tn.read_very_eager().decode('ascii')
print(output)

'''
# 2、打印截屏，此时用 read_all() 不能成功，原因暂时还没完全定位到。
tn.write(b"quit\n")
output = tn.read_all().decode('ascii')
print(output)
'''
# 退出登录
tn.close()
