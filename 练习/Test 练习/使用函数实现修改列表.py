# a_test = ["iphone","xiaomi","microsoft"]
# b_test = []
# while a_test:
#     a_tests = a_test.pop()
#     print("正在打印的模型:" + a_tests)
#     b_test.append(a_tests)
# print("\n已经打印好的模型是:")
# for b_tests in b_test:
#     print(b_tests)


# #通过递归函数实现修改列表的方法
# def a_tests(not_des,en_mods):
#     while not_des:
#         desing = not_des.pop()
#         print("正在打印中的模型：" + desing)
#         en_mods.append(desing)
# def show_en_mod(en_mods):
#     for en_mod in en_mods:
#         print(en_mod)
# not_des = ["iphone","xiaomi","mircosoft"]
# en_mods = []
# a_tests(not_des,en_mods)
# show_en_mod(en_mods)


#传递任意数量的实参
def make_pizza(*toppings):
    print('\nmakeing a pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)
make_pizza('pepperoni')
make_pizza('mogu','1',)

