class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 20
    
    def get_descriptive_name(self):
        lname = str(self.year) + ' ' + self.make + ' ' + self.model
        return lname.title()
    
    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')
    
    #通过方法修改属性的值   
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('U cant roll back!')
    
    #通过方法对属性进行递增
    def increment_odometer(self,miles):
        self.odometer_reading += miles
        
 
 
class Battery():
    def __init__(self,battery = 50):
        self.battery = battery
    def describe_battery(self):
        print('This car has a '+ str(self.battery) + ' kwh battery.') 
        
class Electric_Car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    



tesla = Electric_Car('tesla','model s','2019')
print(tesla.get_descriptive_name())



mcar = Car('audi','a7','2021')
print(mcar.get_descriptive_name())
mcar.update_odometer(30)
mcar.increment_odometer(20)
mcar.read_odometer()
#直接修改方法的值
#mcar.odometer_reading = 30



