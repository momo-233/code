import json

numbers = [1,3,5,7,9,11]
fname = 'd:/programs/code/json存储数据/file/numbers.json'
with open(fname,'w') as object:
    json.dump(numbers,object)