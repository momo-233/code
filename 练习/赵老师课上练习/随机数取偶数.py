import random

x = [random.randint(10,1000) for i in range(10)]
print(x)

y = [i for i in x if i%2==0]

# y = []
# for i in x:
#     if i%2 == 0:
#         y.append(i)


print(y)