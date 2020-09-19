Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "Hello, world!"
>>> print(s)
Hello, world!
>>> x = 5
>>> print(x, s)
5 Hello, world!
>>> s = "Hello,\nworld!"
>>> print(s)
Hello,
world!
>>> len(s)
13
>>> s = "Hello,\tworld!"
>>> print(s)
Hello,	world!
>>> print("\\")
\
>>> print("I\'m a student")
I'm a student
>>> ps
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    ps
NameError: name 'ps' is not defined
>>> s
'Hello,\tworld!'
>>> 
>>> x
5
>>> type(x)
<class 'int'>
>>> y = 15
>>> z = 9
>>> print(x,y,z)
5 15 9
>>> print(x, ':', y, ':', z)
5 : 15 : 9
>>> 