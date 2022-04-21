import re

#log = 'Sep 26 2021 23:11:02-08:00 Layer3Switch-1 L2IFPPI/4/MFLPVLANALARM:OID 1.3.6.1.4.1.2011.5.25.160.3.7 MAC move detected, VlanId = 54, MacAddress = 0000-5e00-0136, Original-Port = GE0/0/1, Flapping port = GE0/0/2. Please check the network accessed to flapping port.'
log3 = 'Sep 26 2021 23:11:02-08:00'
search1 = re.search(r'[0-9][0-9]:[0-9][0-9]:[0-9][0-9]',log3).group()
print(search1)
search2 = re.search(r'\d\d:\d\d:\d\d-\d\d:\d\d',log3)
print(search2)


