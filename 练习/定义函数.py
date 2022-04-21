name = input("请输入你的名字:")
def test_name(name):
    print("Hello " + name.title() + " !")
test_name(name)


def make_shirt(size,word):
    print("A shirt is" + size + "and it hava a" + word)
make_shirt(" XL "," dog")
make_shirt(" L "," cat")


def test_1(name,sex):
    test = name + " " + sex
    return test
full = test_1("momo","man")
print(full)


def person(name,lastname,age=""):
    person2 = {"first":name , "last":lastname}
    if age: 
        person2["age"] = age
    return person2
test = person("momo","meng",age = 21)
print(test)


def person(name,lname):
    person2 = name + lname
    return person2
while 1 == 1:
   name = input("First name: ")
   if name == "q":
       break
   lname = input("Last name: ")
   person1 = person(name,lname)
   print("hello " + person1) 


def tran_users(names):
    for name in names:
        tran ="Hello " + name.title() + " !"
        print(tran)
usernames = ["momo","meng","gui"]
tran_users(usernames)