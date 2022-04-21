from pydoc import stripid
import re

#重复捕获结果测试（按序）
regex0 = r'ipv6 address (\d+)'
regex1 = r'ipv6 address (\d+):\1'
regex2 = r'ipv6 address (\d+):\1:\1'
regex3 = r'ipv6 address (\d+):\1:\1:\1'
regex4 = r'ipv6 address (\d+):\1:\1:\1:\1'
regex5 = r'ipv6 address (\d+):\1:\1:\1:\1:\1'
regex6 = r'ipv6 address (\d+):\1:\1:\1:\1:\1:\1'
regex7 = r'ipv6 address (\d+):\1:\1:\1:\1:\1:\1:\1'
#/1是什么？ 它表示的就是前面捕获组的完全匹配。即前面小括号是啥，这里面就重复什么，例如regex5中有5个/1，加上前面小括号中的(\d+)，一共就是6个

with open(r'D:\programs\code\正则表达式\正则实战\ipv6.txt') as data:
    for line in data:
        #文件读取测试
        #print(line.strip())
        
        match = re.search(regex7,line)
        if match:
            print(line.strip())
            print(match.groups())
            #捕获组（子组）是\d+，即是数字的就能被捕获。关键是\1是啥，它表示的就是前面捕获组的完全匹配。即前面小括号里是啥，这里就重复啥。
            #regex5中有5个\1，加上前面的(\d+)，一共6个。我们可以猜想，ipv6地址中存在6组以上重复的就会被匹配上。
print('\n')        
         
            
#重复捕获结果测试(按名)
regex10 = r'ipv6 address (?P<ipv6>\d+)'
regex11 = r'ipv6 adress (?P<ipv6>\d+):(?P=ipv6)'
regex12 = r'ipv6 address (?P<ipv6>\d+):(?P=ipv6):(?P=ipv6)'
regex13 = r'ipv6 address (?P<ipv6>\d+):(?P=ipv6):(?P=ipv6):(?P=ipv6)'
regex14 = r'ipv6 address (?P<ipv6>\d+):(?P=ipv6):(?P=ipv6):(?P=ipv6):(?P=ipv6)'
regex15 = r'ipv6 address (?P<ipv6>\d+):(?P=ipv6):(?P=ipv6):(?P=ipv6):(?P=ipv6):(?P=ipv6)'
regex16 = r'ipv6 address (?P<ipv6>\d+):(?P=ipv6):(?P=ipv6):(?P=ipv6):(?P=ipv6):(?P=ipv6):(?P=ipv6)'
regex17 = r'ipv6 address (?P<ipv6>\d+):(?P=ipv6):(?P=ipv6):(?P=ipv6):(?P=ipv6):(?P=ipv6):(?P=ipv6):(?P=ipv6)'

with open(r'D:\programs\code\正则表达式\正则实战\ipv6.txt') as data:
    for line in data:
        match = re.search(regex10,line)
        if match:
            print(line.strip())
            print(match.groups())