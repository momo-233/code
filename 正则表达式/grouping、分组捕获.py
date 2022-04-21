import re
#按序分组
line = 'Vlanif1          192.168.11.11/24     up         up'
search1 = re.search('(\S+)\s+([\w.]+)/',line)
print(search1.group(0))
print(search1.group(1))
print(search1.group(2))
#每个括号是一个分组


