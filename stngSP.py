Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> st = "****this is a python language***"
>>> st.strip("*")
'this is a python language'
>>> st.lstrip("*")
'this is a python language***'
>>> st.rstrip("*")
'****this is a python language'
>>> st
'****this is a python language***'
>>> st = st.rstrip("*")
>>> st
'****this is a python language'
>>> st = st.lstrip()
>>> st
'****this is a python language'
>>> st=st.lstrip("*")
>>> st
'this is a python language'
>>> st.split()
['this', 'is', 'a', 'python', 'language']
>>> st.partition()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    st.partition()
TypeError: str.partition() takes exactly one argument (0 given)
st.partition("a")
('this is ', 'a', ' python language')
st.replace("a","q")
'this is q python lqnguqge'
st
'this is a python language'
st.replace("a","q",2)
'this is q python lqnguage'
st.endswith("age")
True
st.startswith("kjhs")
False
st.split()
['this', 'is', 'a', 'python', 'language']
li = st.split()
li
['this', 'is', 'a', 'python', 'language']
" ".join(li)
'this is a python language'
"-".join(li)
'this-is-a-python-language'
