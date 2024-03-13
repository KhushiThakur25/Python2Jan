#single inheritance--a class inherits from only one parent class.

class Parent:
    def show(self):
        print("Hy i'm parent class method..")

class Child(Parent):
    def display(self):
        print("Hey i'm, child class method..")

Ram = Child()
Ram.display()
Ram.show()

#Multiple inheritance--a class acn inherit from multiple parent classes


class Base1:
    def func1(self):
        print("I'm Base 1 class..")
class Base2:
    def func2(self):
        print("I'm Base 2 class..")
class Derived(Base1,Base2):
    def show(self):
        print("I'm Derived class..")

om = Derived()
om.func1()
om.func2()
om.show()

#Multilevel inheritance--a derived class inherits from another derived class..

class GrandParent:
    def func1(self):
        print("I'm GrandParent...")

class Parent(GrandParent):
    def func2(self):
        print("I'm Parent...")

class Child(Parent):
    def func3(self):
        print("I'm Child...")
    
    
Rahul = Child()
Rahul.func1()
Rahul.func2()
Rahul.func3()

#Hierarchical inheritance - multiple dervied classes inherits from a single/parent class

class Animal:
    def speak(self):
        print("Animal speaks")
    
class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("cat meows")


dog = Dog()
dog.speak()
dog.bark()

cat = Cat()
cat.speak()
cat.meow()



    
