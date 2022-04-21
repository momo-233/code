import re

line = 'Hardware address is 4c1f-cc92-675c'
search = re.search(r'[Hh]ard[Ww]are',line).group()
print(search)
search2 = re.search(r'Har',line).group()
print(search2)

commands = ['<Layer3Switch-1>display interface','[Layer3Switch-2]display interface']
for command in commands:
    match = re.search(r'^.+[>\]]',command)
    if match:
        print(match.group())


search3 = re.search(r'[0-9a-zA-Z]+-[0-9a-zA-Z]+-[0-9a-zA-Z]+',line).group()
print(search3)

search4 = re.search(r'[^0-9]+',line).group()
print(search4)
#因为^和[]一起使用，表示不要匹配方括号中的字符, [^0-9]这个正则的意思就是匹配除数字0-9之外的所有字符

        
        