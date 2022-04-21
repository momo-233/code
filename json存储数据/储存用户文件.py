# import json

# username = input('please input u name: ')
# fname = 'd:/programs/code/json存储数据/file/username.json'
# with open(fname,'w') as fobject:
#     json.dump(username,fobject)
#     print('We will remember u when u come back, ' + username + '!')
#     print('Welcome back, ' + username +'!')

import json

#如果以前储存了用户json数据就读取它，否则就提示输入用户名并储存它。
#否则就提示用户输入用户名并储存它

fname = 'd:/programs/code/json存储数据/file/username.json'
try:
    with open(fname) as fobject:
        username = json.load(fobject)
except FileNotFoundError:
    username = input('Please input u name: ')
    with open(fname,'w') as fobject:
        json.dump(username,fobject)
        print('We will remeber u when u come back, ' + username + '!')
else:
    print('Welcome back, ' + username +'!')