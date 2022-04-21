x,y,z=eval(input())
e=x**3+y**3+z**3
if e>1000:
    n=e-1000
    print("please input three numbers:",n)
else:
    n=x+y+z
    print("please input three numbers:",n)