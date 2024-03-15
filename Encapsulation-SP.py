#Private members
#1st method
'''class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    def show(self):
        print("Name:", self.name,"Salary:",self.__salary)
        

emp = Employee("Jasika",10000)
print("name:",emp.name)
print("Salary:",emp.__salary)
emp.show()'''
#2nd method
'''class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

        

emp = Employee("Jasika",10000)
print("name:",emp.name)
print("Salary:",emp._Employee__name)'''

#Protected members

'''class Company:
    def __init__(self):
        self._project = "NLP"

class Employee(Company):
    def __init__(self,name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Employee name:",self.name)
        print("Working on project:",self._project)
c = Employee("Jasika")
c.show()
print("Project:",c._project)
d = Company()
print("Project:",d._project)
'''

#getter and setter

class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    #getter method
    def get_age(self):
        return self.__age
    #setter method
    def set_age(self, age):
        self.__age = age

stud = Student("Jasika",14)

print("Name:",stud.name,stud.get_age())

stud.set_age(16)
print("Name:",stud.name,stud.get_age())


























        














