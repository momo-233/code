def test(name):
    print("Hello " + name + '!')
test('momo') 

def shirt1(size,sentence='test'):
    print('\nThis is a '+size +' size shirt and it have some words ' +sentence)
shirt1('1','2')

#返回值
from os import name
def get_name(onename,lastname):
    name = onename + " " + lastname
    return name.title()
a = get_name('momo','mochine')
print(a)


#返回字典
def persion(surname,name):
    dic_persion = {'xing':surname,'ming':name}
    return dic_persion
a = persion('mo','mo')
print(a) 

def persion(surname,name,age=''):
    dic_persion = {'Surname':surname,'Name':name}
    if age:
       dic_persion['age'] = age
    return dic_persion
a = persion('mo','mo')
print(a) 
