filename = 'd:/programs/code/文件处理/file/write.txt'
with open(filename,'w') as fobject:
    fobject.write('The first of Mochine.\n')
    fobject.write('Mochine is the first.\n')
with open('d:/programs/code/文件处理/file/write.txt') as readobject:
    contents = readobject.read()
    print(contents)
    
