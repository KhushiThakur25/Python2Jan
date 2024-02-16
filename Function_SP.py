'''def add(x,y):
    
    global z
    z = x+y
    print("Sum is:",z)
    #return z
#by default function return "None"
a = add(2,3)
print(a)
print(z)'''


'''def cal(a,b,c):
    d = a+b+c
    print(d)

#cal(5,6,7)
#cal(5,6)
#cal()'''

'''def cal(x = 5,y = 6):
    d = x+y+z
    print("Sum is:",d)

cal()
cal(2)
cal(1,2)
cal(y=6,7)
cal(x = 2,y = 1)'''

#*args = Non-keyword arguments
#**kwargs = keyword arguments
'''def cal(*x):
    print(x)
cal(5,5)
cal(4,5,6,7)
cal(5,6,9,8,7,6,2,1,2)
cal(5)
cal()'''

'''def details(name,age,sal,*address):
    print(name)
    print(age)
    print(sal)
    print(address)

details("Ram",45,45600,"Delhi","chennai","Pune")'''

def person(**details):
    print(details)

person(name = "Kashvi",age = 25)





