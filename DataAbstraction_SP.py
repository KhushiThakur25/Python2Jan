#Data Abstraction
from abc import ABC ,abstractmethod

'''class BaseClass(ABC):
    @abstractmethod
    def show(self):
        pass'''

class Car(ABC):
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def printDetails(self):
        pass
    def accelerate(self):
        print("speed up..")

    def brake(self):
        print("Car stop..")

class HatchBack(Car):
    def printDetails(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Year:",self.year)

    def sunRoof(self):
        print("It doesn't have sunroof..")

class Suv(Car):
    def printDetails(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Year:",self.year)

    def sunRoof(self):
        print("It does have sunroof..")

obj1 = HatchBack("Mahindra","Scorpio","2024")
obj2 = Suv("Maruti","CIAZ","2022")
obj1.printDetails()
obj2.printDetails()
obj1.brake()
obj2.accelerate()

