#字符 | 表示前后两个表达式是**或**的关系
import re

line = 'Hardware address is 4c1f-cc92-675c'
search =re.search(r'Hardware|address',line).group()
print(search)

