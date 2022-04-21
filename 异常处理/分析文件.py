fname = 'd:/programs/code/文件处理/file/Alice.txt'
try:
    with open(fname,'rb') as fobject:
        contents = fobject.read()
except FileNotFoundError:
    print('sorry,this file is not exist.')
else:
    words = contents.split()
    nwords = len(words)
    print('The ' + fname +  ' has about ' + str(nwords) + ' words.') 

