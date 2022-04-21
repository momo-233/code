class Restaurant():
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.number_server = 0
    def describe_restaurant(self):
        print('Our restaurant named ' + self.name +' and its cuisine is ' + self.type)
    def open_restaurant(self):
        print('The ' +self.name + ' is opening')
    def read_server(self):
        print('The restaurant comes ' + str(self.number_server) +' people,this evening.')
    def update_server(self,people):
        self.number_server = people
    def increment_server(self,person):
        self.number_server += person
    
    
r_name = Restaurant('motaurant','china')
r_name.describe_restaurant()
r_name.open_restaurant()
r_name.update_server(30)
r_name.read_server()

y_name = Restaurant('momotaurant','fast')
y_name.describe_restaurant()
y_name.open_restaurant()
r_name.increment_server(15)
r_name.read_server()
