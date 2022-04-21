import random
import time


x=[random.randint(0,10) for i in range(1000000)]
print(x)

#第一种
t1 = int(round(time.time() * 1000))
for i in range(0,11):
    print("%d:%d次" % (i,x.count(i)))
t2 = int(round(time.time() * 1000))
print((t2-t1)/1000)


#第二种
t1 = int(round(time.time() * 1000))
for i in range(0,11):
    h = 0
    for n in x:
        if i==n:
            h+=1
    print("%d:%d次" % (i,h))
t2 = int(round(time.time() * 1000))
print((t2-t1)/1000)
#跑1000000*11次

#第三种
t1 = int(round(time.time() * 1000))
y=[0 for i in range(11)]
for i in x:
    y[i]+=1
for i in range(11):
    print("%d:%d次" % (i,y[i]))
t2 = int(round(time.time() * 1000))
print((t2-t1)/1000)
#跑1000000次