import re
#默认情况下，* + ? 都是贪婪的，即能匹配多，就不匹配少，能匹配越多就匹配越多
line = '<text line> huawei text>'
search = re.search(r'<.*>',line).group()
print(search)
#正则表达式<.*>并没有在line后的>没有停下来，而是在text后的>才停下来。
search2 = re.search(r'<.*?>',line).group()
print(search2)
#如果我们把<.>改成<.*?>的话，则从贪婪变成非贪婪,输出结果  <text line>
