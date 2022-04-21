import re

result = []
regex1 = r'(?P<ip>\d+\.\d+\.\d+\.\d+) +(?P<mac>\w+-\w+-\w+) +.* (?P<port>\S+)'
regex2 = r' + (?P<vlan>\d+)$'

with open('D:\programs\code\正则表达式\正则实战\\dis_arp.txt') as data:
    for line in data:
        #print(line.strip()) 测试文件读取是否向正常
        
        match = re.search(regex2,line)
        if match:
            result[-1].update((match.groupdict()))
            continue
        
        #如果不为vlan字段，则正常查找arp表项
        match = re.search(regex1,line)
        if match:
            result.append(match.groupdict())
            
#补齐上面没有解析出的vlan，让解析更规整，没需求的话可以注释掉
for each_arp_record in result:
    if 'vlan' not in each_arp_record.keys():
        each_arp_record.update(({'vlan':'-'}))

#把结果打印出来展示（亦可以输出到文件或者导入数据库）
print(f'{len(result)} records on arp table :')

#(result,1)找那个的1表示i从1开始，而非从0开始
for i,each_arp_record in enumerate(result,1):
    print(f'\ndetails of arp talbe {i}:')
    for key in each_arp_record:
        print(f'{key:10} : {each_arp_record[key]:10}')
        