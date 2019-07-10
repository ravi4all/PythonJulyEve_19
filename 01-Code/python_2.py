Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Hello world")
Hello world
>>> print("hello","world")
('hello', 'world')
>>> print "hello"
hello
>>> input("Enter your name : ")
Enter your name : Ram

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    input("Enter your name : ")
  File "<string>", line 1, in <module>
NameError: name 'Ram' is not defined
>>> raw_input("Enter your name : ")
Enter your name : Ram
'Ram'
>>> True = "something"
>>> True = False
>>> 
