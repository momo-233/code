import re
log4 = 'MacAddress = 0000-5e00-0136, Original-Port = GE0/0/1, Flapping port = GE0/0/2.'
search1 = re.search(r'0+-\w+-\w+',log4).group()
print(search1)
search2 = re.search(r'(\w+-)+\w+',log4).group()
print(search2)
search3 = re.search(r'(\w+-*)+',log4).group()
print(search3)
search4 = re.search(r'\w+-(\w+-*)+',log4).group()
print(search4)