import time

#destructors: __del__

class Student:
    #constructor
    def __init__(self, name):
        print("Inside the Constructor..")
        self.name = name
        print("Object is initialized here..")
    #method
    def show(self):
        print("Hello , my name is",self.name)
    #destructor
    def __del__(self):
        print("Inside the destructor..")
        print('Object destroyer')

#create object
rahul = Student("Rahul")
ram = rahul
rahul.show()

del rahul

#add sleep and observe the output
time.sleep(5)

print("After sleep")
ram.show()

time.sleep(5)
print("After sleep1")

rahul.show()








