def info_person(name,lastname,age=''):
    info_person_2 = {'first':name,'last':lastname}
    if age:
        info_person_2['age'] = age
    return info_person_2
info_text = info_person('momo','meng',age= 21)
print(info_text)


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(99))