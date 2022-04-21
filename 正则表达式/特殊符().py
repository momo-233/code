import re
line = 'Hardware address is 4c1f-cc92-675c'
search1 = re.search(r'[0-9a-zA-Z]+-[0-9a-zA-Z]+-[0-9a-zA-Z]+', line).group()
print(search1)
search2 = re.search(r'([0-9a-zA-Z])+-([0-9a-zA-Z]+-[0-9a-zA-Z]+)',line).group()
print(search2)