import random



x=[random.randint(0,100) for i in range(1000)]
for i in range(0,101):
    h = 0
    for n in x:
        if i==n:
            h+=1
    print("%d:%d次" % (i,h))

