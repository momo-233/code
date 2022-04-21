import random

print('*'*30)
print("\n\r")
print('欢迎进入澳门赌场')
print("\n\r")
print('*'*30)

usen = input("请输入用户名: ")
money = 0
ans = input("确定进入赌场开始游戏吗？")
if ans == "y" or "Y" or "yes" or "YES" or "确定" or "是":
    # 判断币是否充足
    while money < 2:
        n = int(input("币不足，请充值。(1000港币10币，充值必须是1000的倍数)"))
        # 充值金额判断
        if n%1000 == 0 and n>0:
            money=(n//1000)*10

    print("当前币的数量是(进行一局游戏需要消耗两个币):"+str(money))
    print("进入游戏..........................................")
    money -= 2

    while True:

        # 模拟产生骰子的值
        tz1 = random.randint(1,6)
        tz2 = random.randint(1,6)
        # 两个骰子的值加起来大于6判断为大，小于6判断为小

        print("骰子准备完毕，请猜大小")
        guess = input("请输入大或者小:")

        # 判断
        if (tz1+tz2) > 6 and guess == "大" or ((tz1+tz2) <= 6 and guess == "小"):
            print("恭喜"+usen+"猜中！ 奖励4个游戏币".format(usen))
            money +=4
            print("\n现在币的数量为"+str(money))
        else:
            print("很遗憾，没有猜中。")
            print("\n现在币的数量为"+str(money))

        # 重复开局
        ans = input ("是否再来一局，要扣除两币(y/n)")
        if ans != "y":
            print("退出游戏了")
            break
        else:
            money -= 2
