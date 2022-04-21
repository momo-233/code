a,b,c,d,e,f = map(int,str(input('请输入六位数字:')))
A = (a+b+c+d+e+f)
print (A)

if (A%8)==0:
    print('特等奖')
elif 0<=A<=10:
    print('三等奖')


