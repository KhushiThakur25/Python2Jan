Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> eval('23+7-5')
25
>>> eval('a=5')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    eval('a=5')
  File "<string>", line 1
    a=5
     ^
SyntaxError: invalid syntax
>>> exec('a=5')
>>> a
5
>>> exec('56/54+21')
>>> a = exec('56/54+21')
>>> a
>>> b = eval('65-5')
>>> b
60
>>> a = ["Ram","Amit","Om","Aman"]
>>> b = [45,30,25,22]
>>> zip(a,b)
<zip object at 0x0000024BE3F60480>
>>> s = zip(a,b)
>>> set(s)
{('Aman', 22), ('Ram', 45), ('Om', 25), ('Amit', 30)}
tuple(s)
()
s
<zip object at 0x0000024BE67BE0C0>
s = zip(a,b)
s
<zip object at 0x0000024BE45C3EC0>
set(tuple(s))
{('Aman', 22), ('Ram', 45), ('Om', 25), ('Amit', 30)}
s = zip(a,b)
dict(s)
{'Ram': 45, 'Amit': 30, 'Om': 25, 'Aman': 22}
a = ["Ram","Amit","Om","Aman"]
b = [45,30,25,22,65,87]
s = zip(a,b)
list(s)
[('Ram', 45), ('Amit', 30), ('Om', 25), ('Aman', 22)]
for i in enumerate(len(a)):
    print(a[i])

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    for i in enumerate(len(a)):
TypeError: 'int' object is not iterable
for i in enumerate(a):
    print(a[i])

Traceback (most recent call last):
  File "<pyshell#31>", line 2, in <module>
    print(a[i])
TypeError: list indices must be integers or slices, not tuple
for i in range(len(a)):
    print(a[i])

Ram
Amit
Om
Aman
list(enumerate(a))
[(0, 'Ram'), (1, 'Amit'), (2, 'Om'), (3, 'Aman')]
enumerate(a)
<enumerate object at 0x0000024BE68B24D0>

for i in range(len(a)):
    print(i,a[i])

0 Ram
1 Amit
2 Om
3 Aman
list(enumerate(a,100))
[(100, 'Ram'), (101, 'Amit'), (102, 'Om'), (103, 'Aman')]
tuple(enumerate(a,100))
((100, 'Ram'), (101, 'Amit'), (102, 'Om'), (103, 'Aman'))
dict(enumerate(a,100))
{100: 'Ram', 101: 'Amit', 102: 'Om', 103: 'Aman'}
