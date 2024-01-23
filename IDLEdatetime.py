Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Python312/ChatAppSP.py
Enter your message..:bye
Bye user
import datetime
datetime.datetime
<class 'datetime.datetime'>
datetime.datetime.now()
datetime.datetime(2024, 1, 23, 14, 31, 59, 570173)
datetime.datetime.now().date
<built-in method date of datetime.datetime object at 0x000002195AFBC840>
datetime.datetime.now().date()
datetime.date(2024, 1, 23)
datetime.datetime.now().time()
datetime.time(14, 33, 49, 28815)
>>> from datetime import datetime as dt
>>> dt
<class 'datetime.datetime'>
>>> dt.now().date()
datetime.date(2024, 1, 23)
>>> date = dt.now().date()
>>> time = dt.now().time()
>>> print(date)
2024-01-23
>>> print(time)
14:37:01.617005
>>> date.strftime("%d/%m/%y")
'23/01/24'
>>> date.strftime("%d/%b/%y")
'23/Jan/24'
>>> date.strftime("%d/%B/%y")
'23/January/24'
>>> date.strftime("%d/%B/%Y")
'23/January/2024'
>>> date.strftime("%d/%B/%Y,%a")
'23/January/2024,Tue'
>>> date.strftime("%d/%B/%Y,%A")
'23/January/2024,Tuesday'
>>> time.strftime("%H : %M : %S")
'14 : 37 : 01'
>>> time.strftime("%H :%M :%S,%p")
'14 :37 :01,PM'
