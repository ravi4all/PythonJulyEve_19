Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello world this is python programming. Python is used for data science"
>>> x = "hello"
>>> y = "hello"
>>> id(x)
2222542189040
>>> id(y)
2222542189040
>>> x == y
True
>>> x is y
True
>>> x[0]
'h'
>>> x[1]
'e'
>>> x[100]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x[100]
IndexError: string index out of range
>>> len(x)
5
>>> x
'hello'
>>> x[0] = 'X'
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x[0] = 'X'
TypeError: 'str' object does not support item assignment
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    del x[0]
TypeError: 'str' object doesn't support item deletion
>>> x
'hello'
>>> x = x + "world"
>>> x
'helloworld'
>>> x = "hello"
>>> id(x)
2222542189040
>>> x =  x + "world"
>>> id(x)
2222542220336
>>> x * 5
'helloworldhelloworldhelloworldhelloworldhelloworld'
>>> x = "hello world"
>>> x[0:4]
'hell'
>>> x[2:4]
'll'
>>> x[4:4]
''
>>> x[0:4]
'hell'
>>> x[0:10:2]
'hlowr'
>>> x
'hello world'
>>> x[-1]
'd'
>>> x[0:-1]
'hello worl'
>>> x[:]
'hello world'
>>> x[0:100]
'hello world'
>>> x[10:0]
''
>>> x[10:0:-1]
'dlrow olle'
>>> x[10::-1]
'dlrow olleh'
>>> x[-1:-8]
''
>>> x[-1:-8:-1]
'dlrow o'
>>> x[-8:-1]
'lo worl'
>>> text
'hello world this is python programming. Python is used for data science'
>>> text.lower()
'hello world this is python programming. python is used for data science'
>>> text.upper()
'HELLO WORLD THIS IS PYTHON PROGRAMMING. PYTHON IS USED FOR DATA SCIENCE'
>>> text.capitalize()
'Hello world this is python programming. python is used for data science'
>>> text.title()
'Hello World This Is Python Programming. Python Is Used For Data Science'
>>> text.count('o')
6
>>> text.find('o')
4
>>> text.find('o',5)
7
>>> text.find('o',8)
24
>>> text.find('o',25)
29
>>> text.rfind('o')
56
>>> len(text)
71
>>> text.split()
['hello', 'world', 'this', 'is', 'python', 'programming.', 'Python', 'is', 'used', 'for', 'data', 'science']
>>> text = text.split()
>>> text
['hello', 'world', 'this', 'is', 'python', 'programming.', 'Python', 'is', 'used', 'for', 'data', 'science']
>>> '-'.join(text)
'hello-world-this-is-python-programming.-Python-is-used-for-data-science'
>>> x = ["ram","works","in","IT","dept"]
>>> ' '.join(x)
'ram works in IT dept'
>>> '#'.join(x)
'ram#works#in#IT#dept'
>>> x = '#'.join(x)
>>> x
'ram#works#in#IT#dept'
>>> x.replace('#',' ')
'ram works in IT dept'
>>> x  = x.replace('#',' ')
>>> x
'ram works in IT dept'
>>> x.center(40)
'          ram works in IT dept          '
>>> len(x)
20
>>> x.center(20)
'ram works in IT dept'
>>> x.center(21)
' ram works in IT dept'
>>> x.center(22)
' ram works in IT dept '
>>> x.center(40)
'          ram works in IT dept          '
>>> x.center(40,'*')
'**********ram works in IT dept**********'
>>> x.center(40,'#')
'##########ram works in IT dept##########'
>>> x
'ram works in IT dept'
>>> x.isalpha()
False
>>> x.isdecimal()
False
>>> x.islower()
False
>>> x.startswith('y')
False
>>> x
'ram works in IT dept'
>>> x.startswith('ram')
True
>>> x.endswith('dept')
True
>>> 
