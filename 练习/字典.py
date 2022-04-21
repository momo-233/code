from typing import Hashable


test_0 = {"color":"green","points":5}
test_0["x_zhou"] = 0
test_0["y_zhou"] = 25
print(test_0)
n_points = test_0["points"]
print("你的得分是"+str(n_points)) 

#修改字典中的值
test_0 = {"color":"green","points":5}
test_0["color"] = "黄色"
print("外星飞船的颜色是" + test_0["color"])

#删除键-值对
test_0 = {"color":"green","points":5}
del test_0["points"]
print(test_0)

#由类似对象组成的对象
最喜欢的语言 = {
    "kai":"java",
    "meng":"python",
    "long":"c++",
    "mt":"c++",
}
print("我最喜欢的语言是"+最喜欢的语言["meng"].title())

最喜欢的语言 = {
    "kai":"java",
    "meng":"python",
    "long":"c++",
    "mt":"c++",
}
for key, value in 最喜欢的语言.items():
    print("\nKey:" + key)
    print("Value:" + value)

