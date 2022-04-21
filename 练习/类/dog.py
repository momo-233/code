class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age    
        
    def sit(self):
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        print(self.name.title() + ' rolled over!')


dog1 = Dog('lili',2)
dog1.sit()
dog1.roll_over()

dog2 = Dog('lele',2)
dog2.sit()
dog2.roll_over