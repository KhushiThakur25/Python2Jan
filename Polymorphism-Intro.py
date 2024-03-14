#Polymorphism..

class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I m a cat.My name {self.name}. I am {self.age} years old")

    def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I m a Dog.My name {self.name}. I am {self.age} years old")

    def make_sound(self):
        print("Bark")

cat1 = Cat("Kitty",2.5)
dog1 = Dog("Tom",4)
cat2 = Cat("Snowy",3)

for animal in (cat1,dog1,cat2):
    animal.make_sound()
    animal.info()
    















