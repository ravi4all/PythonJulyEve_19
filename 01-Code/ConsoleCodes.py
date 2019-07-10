Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/July/01-Code/01-class.py 
33
>>> print("Hello world")
Hello world
>>> print("Hello","World")
Hello World
>>> print "hello"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hello")?
>>> input("Enter your name : ")
Enter your name : Ram
'Ram'
>>> a = True
>>> True = "something"
SyntaxError: can't assign to keyword
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/July/01-Code/01-class.py 
33
Sum is 33
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/July/01-Code/01-class.py 
33
Sum is 33
Sum is 33
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/July/01-Code/01-class.py 
33
Sum is 33
Sum is 33
Sum of 12 and 21 is 33
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/July/01-Code/01-class.py 
33
Sum is 33
Sum is 33
Sum of 12 and 21 is 33
Sum of 12 and 21 is 33
>>> name = "Ravi"
>>> msg  = "Hello " + name
>>> msg
'Hello Ravi'
>>> sal = 10000
>>> msg = "Hello "+name+"Salary is"+sal
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    msg = "Hello "+name+"Salary is"+sal
TypeError: can only concatenate str (not "int") to str
>>> msg = "Hello {}".format(name)
>>> msg
'Hello Ravi'
>>> msg = "Hello {} Your salary is {}".format(name, sal)
>>> msg
'Hello Ravi Your salary is 10000'
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/July/01-Code/01-class.py 
33
Sum is 33
Sum is 33
Sum of 12 and 21 is 33
Sum of 12 and 21 is 33
Sum of 12 and 21 is 33
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/July/01-Code/01-class.py 
33
Sum is 33
Sum is 33
Sum of 12 and 21 is 33
Sum of 12 and 21 is 33
Sum of 12 and 21 is 33
Sum of 21 and 12 is 33
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/July/01-Code/01-class.py 
33
Sum is 33
Sum is 33
Sum of 12 and 21 is 33
Sum of 12 and 21 is 33
Sum of 12 and 21 is 33
Sum of 21 and 12 is 33
Sum of 12 and 21 is 33
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/July/01-Code/02-class.py 
Enter your name : Ram
Hello Ram
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/July/01-Code/02-class.py 
Enter your name : Ram
Hello Ram
Enter first number : 12
Enter second number : 77
1277
>>> f
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    f
NameError: name 'f' is not defined
>>> f_num
'12'
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/July/01-Code/02-class.py 
Enter your name : Ram
Hello Ram
Enter first number : 12
Enter second number : 23
35
>>> a = 12
>>> type(a)
<class 'int'>
>>> isinstance(a, int)
True
>>> id(a)
140708156761072
>>> id(12)
140708156761072
>>> a = "hello world"
>>> print(a)
hello world
>>> a = "hello "world""
SyntaxError: invalid syntax
>>> a = 'hello "world"'
>>> print(a)
hello "world"
>>> a = ""'hello "world"'""
>>> print(a)
hello "world"
>>> a = ''''hello "world"''''
SyntaxError: EOL while scanning string literal
>>> a = """'hello "world"'"""
>>> print(a)
'hello "world"'
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/July/01-Code/03-class.py 

1. Add
2. Sub
3. Div
4. Mul


 public class BagOfWordsVectorizer extends BaseTextVectorizer {
      public BagOfWordsVectorizer(){}
      protected BagOfWordsVectorizer(VocabCache cache,
             TokenizerFactory tokenizerFactory,
             List<String> stopWords,
             int minWordFrequency,
             DocumentIterator docIter,
             SentenceIterator sentenceIterator,
             List<String> labels,
             InvertedIndex index,
             int batchSize,
             double sample,
             boolean stem,

>>> path = "C:\Python37\Lib\asyncio"
>>> import os
>>> os.chdir(path)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    os.chdir(path)
OSError: [WinError 123] The filename, directory name, or volume label syntax is incorrect: 'C:\\Python37\\Lib\x07syncio'
>>> 
>>> a = "hello \n world"
>>> print(a)
hello 
 world
>>> a = "hello \\n world"
>>> print(a)
hello \n world
>>> os.getcwd()
'C:\\Users\\asus\\Documents\\Data\\DataTransfer\\BMPL_Batches\\2019\\July\\01-Code'
>>> path = "C:/Python37/Lib/asyncio"
>>> os.chdir(path)
>>> path = r"C:\Users\asus\Documents\Data\DataTransfer\BMPL_Batches\2019\July\01-Code"
>>> os.chdir(path)
>>> 
