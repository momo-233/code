import re

# string1 = 'abbbaccc'
# search1 = re.search(r'ac*',string1).group()
# print(search1)

#通过重复符*匹配筛选多级邮箱后缀
email1 = 'mochine233@abc.com'
email2 = 'mochine233@gd.abc.com'
email3 = 'mochine233@st.gd.abc.com'

search1 = re.search(r'\S+@(\w+\.)*com',email1).group()
print(search1)

search2 = re.search(r'\S+@(\w+\.)*com',email2).group()
#通过(\w+\.)* 来匹配邮箱中的多级后缀，因为*可以匹配多次或者直接略过/理解/
print(search2)

search3 = re.search(r'\S+@(\w+\.)*com',email3).group()
print(search3)
#search3，同理search2，通过*达到多次匹配的规则


##重复符？匹配多级邮箱后缀
search4 = re.search(r'\S+@(\w+\.)?com',email1).group()
print(search4)
search5 = re.search(r'\S+@(\w+\.)+com',email2).group()
print(search5)
search6 = re.search(r'\S+@\S+com',email3).group()
print(search6)