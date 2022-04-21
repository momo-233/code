import re
from typing import Match

log2 = 'VlanId = 54, MacAddress = 0000-5e00-0136, Original-Port = GE0/0/1, Flapping port = GE0/0/2. '
re_template = r'VlanId = (\d+), MacAddress = (\S+), Original-Port = (\S+), Flapping port = (\S+)\.'
match = re.search(re_template,log2)
print(match.group())

#.group()的扩展用法
print(match.group(0))
print(match.group(1))
print(match.group(2))
print(match.group(3))
print(match.group(4))
try:
    print(match.group(5))
except IndexError:
    print(match.groups())
#最后再用一下groups()
