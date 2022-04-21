#逆正整数
nmu = input("请输入一个正整数:")
print("逆正整数为:"+nmu[::-1])

#在列表之间移动元素
待验证列表 = ["momochine","mochine","momo"]
已认证列表 = []
while 待验证列表:
    已验证列表 = 待验证列表.pop()
    print ("已经完成认证的用户: "+已验证列表.title())
    已认证列表.append(已验证列表)
print("\n用户已经完成确认: ")
for 已验证列表 in 已认证列表:
    print(已验证列表.title())