tests=[1,2,3]
for test in tests:
    print(str(test)+",is a number")
print("They are all of the number")

高 = str(input("请输入身高:"))
体重 = str(input("请输入体重:"))
bmi = 体重/(2**2)
if bmi < 18.5:
    print("过轻")
elif bmi <=25:
    print("正常")
else:
    print("肥胖")
    
