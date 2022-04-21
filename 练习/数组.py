tests=[1,2,3]
for test in tests:
    test = test + 1
    print(test)
    
a = [3,1,2,5,7,4]
m = a[0]
n = a[0]
for a1 in a:
    if a1>m:    
        m = a1
    if a1<n:
        n = a1
    print("数组的最大值是:" + str(n))
    print("数组的最小值是:" + str(m))
