import re

log4 = 'MAC move detected, VlanId = 54, MacAddress = 0000-5e00-0136,'
search1 = re.search(r'[a-z0-9][a-z0-9][a-z0-9][a-z0-9]-[a-z0-9][a-z0-9][a-z0-9][a-z0-9]-[a-z0-9][a-z0-9][a-z0-9][a-z0-9]',log4).group()
print(search1)
search2 = re.search(r'\w\w\w\w-\w\w\w\w-\w\w\w\w',log4)
print(search2)