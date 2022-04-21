#切片增加
list1 = [3,5,7]
list1[:0] = [1,2]
print(list1)

#切片替换
list2 = [3,5,7,9,11]
list2[::2] = ['a','b','c']
print(list2)

#切片删除
list3=[1,3,5,7,9]
list3[:2] = []
print(list3)



