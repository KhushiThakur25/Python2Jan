Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tup = (1,2,3,4)
>>> type(tup)
<class 'tuple'>
>>> a = tuple()
>>> type(a)
<class 'tuple'>
>>> a
()
>>> h = 41,54,69,35
>>> type(h)
<class 'tuple'>
>>> tup[0]
1
>>> tup[3]
4
>>> tup[0] = 100
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    tup[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> tup.append(100)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    tup.append(100)
AttributeError: 'tuple' object has no attribute 'append'
len(tup)
4
tup.count(2)
1
tup.index(2)
1
tup.find(2)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    tup.find(2)
AttributeError: 'tuple' object has no attribute 'find'
tup.max()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tup.max()
AttributeError: 'tuple' object has no attribute 'max'
max(tup)
4
sum(tup)
10
min(tup)
1
list(tup)
[1, 2, 3, 4]
type(tup)
<class 'tuple'>
tup = list(tup)
type(tup)
<class 'list'>
tup.append(100)
tup
[1, 2, 3, 4, 100]
tup[0] = 105
tup
[105, 2, 3, 4, 100]
tup.insert(2,65)
tup
[105, 2, 65, 3, 4, 100]
tup.pop()
100
tup
[105, 2, 65, 3, 4]
tup.remove(3)
tup
[105, 2, 65, 4]
tup = tuple(tup)
tup
(105, 2, 65, 4)
