def even(num):
    return num%2 == 0
def odd(num):
    return num%2 != 0

numbers = [42,56,33,69,47,21,321,147,22,84]
print(list(filter(even , numbers)))
print(list(filter(odd , numbers)))


'''lambda - keyword it is used to create a single line function..

syntax - lambda argument:expression'''


n = [1,2,3,4,5]

print(list(map(lambda x: x**2 , n)))

li_1 = ["Ram ","Amit ","Aman "]
li_2 = ["Singh","Srivastava","Tyagi"]

li = list(map(lambda x,y: x+y ,li_1,li_2))

print(li)
