# #字典列表
# 外星人_0={"color":"green","points":5}
# 外星人_1={"color":"blue","points":10}
# 外星人_2={"color":"red","points":15}
# 外星人=[外星人_0,外星人_1,外星人_2]
# for 外星人test in 外星人:
#     print(外星人test)

# #range()生成外星人
# 外星人们=[]
# for 外星人_号码 in range(30):
#     新的外星人={"color":"green","points":5,"speed":"slow"}
#     外星人们.append(新的外星人)
# for 外星人 in 外星人们[:0]:
#     print(外星人)

#修改创建的外星人
外星人们=[]
for 外星人_号码 in range(30):
    新的外星人={"color":"green","points":5,"speed":"slow"}
    外星人们.append(新的外星人)
for 外星人 in 外星人们[0:7]:
    if 外星人["color"] == "green":
        外星人["color"] ="yello"
        外星人["speed"] = "medium"
        外星人["points"] = "10"
for 外星人 in 外星人们[0:7]:
    print(外星人)

