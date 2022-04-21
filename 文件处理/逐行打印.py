fname = 'd:/programs/code/文件处理/file/test.txt'
with open(fname) as fobject:
    for line in fobject:
        print(line.rstrip())
        
#创建一个包含文件各行内容的列表
fname = 'd:/programs/code/文件处理/file/test.txt'
with open(fname) as fobject:
    lines = fobject.readlines()
for line in lines:
    print(line.rstrip())