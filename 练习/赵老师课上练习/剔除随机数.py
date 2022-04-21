import random


x=[random.randint(0,100) for i in range(100)]
print(x)
for y in x:
    if x.count(y)>1:
        x.remove(y)
print(x)
     
