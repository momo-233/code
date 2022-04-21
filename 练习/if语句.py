from typing import overload


companys=["sony","nintendo","microsoft"]
for company in companys:
    if company != "nintendo":
        print(company.upper())
    else:
        print(company.title()) 

age=14
if age >= 18:
    print ("u old is enough to vote！")
else:
    print("u old is not enough")


age=3
if age< 4:
    print("免费")
elif age< 18:
    print("收费五元")
else:
    print("收费10元")


列表=["榴莲","鸡肉"]
if 列表:
    for 材料 in 列表:
        print("加"+ 材料)
    print("\n感谢您点餐")
else:
    print("你是不是想要一个披萨")

