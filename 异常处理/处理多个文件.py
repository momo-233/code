def count_words(fname):
    try:
        with open(fname,'rb') as fobject:
            contents = fobject.read()
    except FileNotFoundError:
        print('sorry,this file is not exist.')
    else:
        words = contents.split()
        nwords = len(words)
        print('The ' + fname +  ' has about ' + str(nwords) + ' words.')
        
fnames = ['d:/programs/code/文件处理/file/Moby Dick.txt','d:/programs/code/文件处理/file/Alice.txt','Alice.txt']
for fname in fnames:
    count_words(fname)