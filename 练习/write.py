#输入
f = open('D:\\1.txt','w')
f.write('python,test.\ntest2!')
f.close()

#迭代器遍历文件结构
f = open('D:\\1.txt','r')
for line in f:
    print(line,end='')
f.close()