fname = 'd:/programs/code/文件处理/file/test.txt'
with open(fname) as fobject:
    lines = fobject.readlines()
pistring = ''
for line in lines:
    pistring += line.rstrip()    
print(pistring)
print(len(pistring))

#删除左行空格
fname = 'd:/programs/code/文件处理/file/test.txt'
with open(fname) as fobject:
    lines = fobject.readlines()
pistring = ''
for line in lines:
    pistring += line.strip()
print('\n',pistring)
print(len(pistring))