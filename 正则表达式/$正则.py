import re
line = 'Hardware address is 4c1f-cc92-675c'
search = re.search(r'\S+$',line).group()
print(search)