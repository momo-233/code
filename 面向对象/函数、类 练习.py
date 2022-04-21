class Bugs():
    def __init__(self,active,things):
        self.active = active
        self.things = things
    def makebugs(self):
        print('The following pass is ' + self.active + ' and is completed ' + self.things)
    
new_bugs = Bugs('print','output')
new_bugs.makebugs()