import re
line = 'Vlanif1          192.168.11.11/24     up         up'
search = re.search(r'(\S+)\s+([\w.]+)/',line).group()
print(search)