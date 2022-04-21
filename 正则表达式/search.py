import re

#match = re.search(pattern,string,flags=0)
line = 'Route Port,The Maximum Transmit Unit is 1500'
match = re.search('The Maximum Transmit Unit is \d+',line)
match2 = re.search('The Maximum Transmittest',line)
print(match)
print(match.group())
print(match2)
