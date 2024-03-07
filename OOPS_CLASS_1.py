#how to define classes

class Car:
    #constructor-it is used for initializing the attributes
    def __init__(self,*args):
        if len(args)==1:
            self.windows = args[0]
        elif len(args)==2:
            self.windows = args[0]
            self.tyres = args[1]
        elif len(args)==3:
            self.windows = args[0]
            self.tyres = args[1]
            self.engine = args[2]

            
    def make_sound(self,sound):
        return "The car has {} windows and sound {}".format(self.windows,sound)
    


        
    '''def __init__(self,windows,tyres,engine):
        self.windows = windows
        self.tyres = tyres
        self.engine = engine'''
        
    '''def __init__(self,windows,tyres):
        self.windows = windows
        self.tyres = tyres
        #self.engine = engine'''
    

car1 = Car(4,6,"petrol")
'''car2 = Car(6,6,"diesel")
car3 = Car(8)'''

'''car1.windows = 4
car1.tyres = 4
car1.engine = "diesel"

car2.windows = 6
car2.tyres = 6
car2.engine = "petrol"

car3.windows = 8
car3.tyres = 8
car3.engine = "CNG"'''

print(car1.windows)
print(car1.tyres)
print(car1.engine)
print(car1.make_sound("wroom wroom"))




