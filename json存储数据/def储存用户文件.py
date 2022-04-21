import json
def getusername():
    fname = 'd:/programs/code/json存储数据/file/username.json'
    try:
        with open(fname) as fobject:
            username = json.load(fobject)
    except FileNotFoundError:
        return None
    else:
        return username
    
def newusername():
    username = input('Please input u name: ')
    fname = 'd:/programs/code/json存储数据/file/username.json'
    with open(fname,'w') as fobject:
        json.dump(username,fobject)
    return username

def greetuser():
    username = getusername()
    if username:
        print('Welcome back ' + username + '!')
    else:
        username = newusername()
        print('We will remeber u when u come back, ' + username + '!')
greetuser()