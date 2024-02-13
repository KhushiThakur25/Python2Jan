Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> st = {}
>>> type(st)
<class 'dict'>
>>> a = set()
>>> type(a)
<class 'set'>
>>> a
set()
>>> set_1 = {1,2,3,4,5,5}
>>> set_1
{1, 2, 3, 4, 5}
>>> set_ = {3,4,5,6,7}
>>> set_2 = {3,4,5,6,7}
>>> set_1.union(set_2)
{1, 2, 3, 4, 5, 6, 7}
>>> set_1.update(set_2)
>>> set_1
{1, 2, 3, 4, 5, 6, 7}
>>> set_1 = {1,2,3,4,5,5}
>>> set_1.intersection(set_2)
{3, 4, 5}
>>> set_1
{1, 2, 3, 4, 5}
>>> set_2
{3, 4, 5, 6, 7}
set_1.intersection_update()set_2
SyntaxError: incomplete input
SyntaxError: incomplete input
SyntaxError: incomplete input


set_1.intersection_update(set_2)
set_1
{3, 4, 5}
set_1 = {1,2,3,4,5,5}
set_1.difference(set_2)
{1, 2}
set_1.isdisjoint(set_2)
False
set_2 = {8,9}
set_1.isdisjoint(set_2)
True
set_2 = {2,3}
set_1.issuperset(set_2)
True
set_2 = {2,3,9}
set_1.issuperset(set_2)
False
set_2 = {2,3}
set_1.issubset(set_2)
False
set_2.issubset(set_1)
True
del set_1
set_1
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    set_1
NameError: name 'set_1' is not defined. Did you mean: 'set_'?
set_2
{2, 3}
set_2.clear()
set_2
set()
set_2.add(65)
set_2
{65}
set_2.add(32)
set_2.add(32,6,8)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    set_2.add(32,6,8)
TypeError: set.add() takes exactly one argument (3 given)
set_2.add([32,6,8])
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    set_2.add([32,6,8])
TypeError: unhashable type: 'list'
set_2.add(3)
set_2.add(2)
set_2.add(5)
set_2
{32, 65, 2, 3, 5}
set_2.pop()
32
set_2.remove(2)
set_2
{65, 3, 5}
set_2.remove(9)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    set_2.remove(9)
KeyError: 9
set_2.discard(9)
set_2 = {32, 65, 2, 3, 5}
set_2.pop()
32
set_2.pop()
65
set_2.pop()
2
a = dict()
type(a)
<class 'dict'>
a
{}
dict_1 = {"name":}
SyntaxError: incomplete input
dict_
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    dict_
NameError: name 'dict_' is not defined. Did you mean: 'dict'?
dict_1 = {"name":"Ram","class":5,"Roll no":32}
dict_1
{'name': 'Ram', 'class': 5, 'Roll no': 32}
dict_1 = "name"
dict_1
'name'
type(dict_1)
<class 'str'>
dict_1 = {"name":"Ram","class":5,"Roll no":32}
type(dict_1)
<class 'dict'>
dict_1{"name"}
SyntaxError: invalid syntax
dict_1["name"]
'Ram'
dict_1["name"] = "RAMAN"
dict_1
{'name': 'RAMAN', 'class': 5, 'Roll no': 32}
dict_1["marks"] = 78
dict_1
{'name': 'RAMAN', 'class': 5, 'Roll no': 32, 'marks': 78}
dict_1.keys()
dict_keys(['name', 'class', 'Roll no', 'marks'])
dict_1.values()
dict_values(['RAMAN', 5, 32, 78])
dict_1.items()
dict_items([('name', 'RAMAN'), ('class', 5), ('Roll no', 32), ('marks', 78)])
len(dict_1)
4
dict_1[2]
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    dict_1[2]
KeyError: 2
dict_1.get()
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    dict_1.get()
TypeError: get expected at least 1 argument, got 0
dict_1.get("name")
'RAMAN'
dict_1.get("name","class")
'RAMAN'
dict_1.get("name","class")
'RAMAN'
dict_1.clear()
dict_1
{}
dict_1 = {"name":"Ram","class":5,"Roll no":32}
dict_1.pop()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    dict_1.pop()
TypeError: pop expected at least 1 argument, got 0
dict_1.pop("class")
5
dict_1.popitem()
('Roll no', 32)
dict_1 =  {"name":"Ram","class":5,"Roll no":32}
dict_2 = {5:2,65:3,89:4}
dict_2
{5: 2, 65: 3, 89: 4}
dict_1.update(dict_2)
dict_1
{'name': 'Ram', 'class': 5, 'Roll no': 32, 5: 2, 65: 3, 89: 4}
m = dict_1.copy()
m
{'name': 'Ram', 'class': 5, 'Roll no': 32, 5: 2, 65: 3, 89: 4}
del dict_1
dict_1
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    dict_1
NameError: name 'dict_1' is not defined. Did you mean: 'dict_2'?
