fname = 'd:/programs/code/文件处理/file/write.txt'
with open(fname,'a') as fobject:
    fobject.write('Print test!.\n')
with open('d:/programs/code/文件处理/file/write.txt') as readobject:
    contents = readobject.read()
    print(contents)