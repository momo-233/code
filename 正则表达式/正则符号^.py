#字符^表示行首， ^\d+ 表示以数字开头
import re

mac = '2, Hardware address is 4c1f-cc92-675c'
search = re.search(r'^\d+',mac).group()
print(search)

prompt = '<Layer3Switch-1>display interface'
search2 = re.search(r'^.+>',prompt).group()
print(search2)
# '^.+' 应用
#通常我们使用^来截取从开头到特定符号（包括特定符号