#使用标志
message0 = "\nTell me something，and I will repeat it back to u"
message0 += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(message0)
    if message == 'quit':
        active = False
    else:
        print(message)

#让用户选择何时退出
message0 = "\nTell me something，and I will repeat it back to u"
message0 += "\nEnter 'quit' to end the program. "
message1 = ""
while message1 != 'quit':
    message1 = input(message0)
    print (message1)

#用break退出循环
mess = "\nPlease enter the name of a city you have visited: "
mess += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(mess)
    if city  == 'quit':
        break
    else:
        print("I 'd love to go to " + city.title() + "!")

#使用continue继续循环
test_num = 0
while test_num < 10:
    test_num += 1
    if test_num % 2 == 0:
        continue
    print(test_num)

