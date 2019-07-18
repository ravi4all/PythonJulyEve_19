Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = []
>>> type(x)
<class 'list'>
>>> x = [4,5,3,3,7,5,4,2,45,6,32,56,87,34]
>>> x = [4,5,3,3,7,5,4,2,45,6,32,56,87,34,23.44,33.44]
>>> x = [4,5,3,3,7,5,4,2,45,6,32,56,87,34,23.44,33.44,"hello"]
>>> x = [4,5,3,3,7,5,4,2,45,6,32,56,87,34,23.44,33.44,"hello",True]
>>> x
[4, 5, 3, 3, 7, 5, 4, 2, 45, 6, 32, 56, 87, 34, 23.44, 33.44, 'hello', True]
>>> x[0]
4
>>> x[0:5]
[4, 5, 3, 3, 7]
>>> x[10::-1]
[32, 6, 45, 2, 4, 5, 7, 3, 3, 5, 4]
>>> x = []
>>> x.append(50)
>>> x
[50]
>>> x.append(23)
>>> x
[50, 23]
>>> x.append(74)
>>> x
[50, 23, 74]
>>> x.append(72)
>>> x.append(21)
>>> x.append(65)
>>> x
[50, 23, 74, 72, 21, 65]
>>> x.append(56,234,7,3,6,7,5,4)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    x.append(56,234,7,3,6,7,5,4)
TypeError: append() takes exactly one argument (8 given)
>>> x.append(100)
>>> x
[50, 23, 74, 72, 21, 65, 100]
>>> x[-1]
100
>>> x.pop()
100
>>> x
[50, 23, 74, 72, 21, 65]
>>> x.pop()
65
>>> x
[50, 23, 74, 72, 21]
>>> x.pop(3)
72
>>> x
[50, 23, 74, 21]
>>> x.append([43,44,65,61,32])
>>> x
[50, 23, 74, 21, [43, 44, 65, 61, 32]]
>>> x.append([34,41,54,18,29])
>>> x
[50, 23, 74, 21, [43, 44, 65, 61, 32], [34, 41, 54, 18, 29]]
>>> x.pop()
[34, 41, 54, 18, 29]
>>> x
[50, 23, 74, 21, [43, 44, 65, 61, 32]]
>>> x.append([34,41,54,18,29])
>>> x
[50, 23, 74, 21, [43, 44, 65, 61, 32], [34, 41, 54, 18, 29]]
>>> x[-1]
[34, 41, 54, 18, 29]
>>> x[-1].append(44)
>>> x
[50, 23, 74, 21, [43, 44, 65, 61, 32], [34, 41, 54, 18, 29, 44]]
>>> x[-1].append([44,7,8,5,34,4,6])
>>> x
[50, 23, 74, 21, [43, 44, 65, 61, 32], [34, 41, 54, 18, 29, 44, [44, 7, 8, 5, 34, 4, 6]]]
>>> x[-1]
[34, 41, 54, 18, 29, 44, [44, 7, 8, 5, 34, 4, 6]]
>>> x[-1][-1]
[44, 7, 8, 5, 34, 4, 6]
>>> x[-1][-1][-1]
6
>>> x[-1][-1].pop()
6
>>> x[-1].pop()
[44, 7, 8, 5, 34, 4]
>>> x
[50, 23, 74, 21, [43, 44, 65, 61, 32], [34, 41, 54, 18, 29, 44]]
>>> x.pop()
[34, 41, 54, 18, 29, 44]
>>> x.pop()
[43, 44, 65, 61, 32]
>>> x
[50, 23, 74, 21]
>>> x.extend([44,7,8,5,34,4,6])
>>> x
[50, 23, 74, 21, 44, 7, 8, 5, 34, 4, 6]
>>> x.insert(3,90)
>>> x
[50, 23, 74, 90, 21, 44, 7, 8, 5, 34, 4, 6]
>>> x.index(44)
5
>>> x.remove(44)
>>> x
[50, 23, 74, 90, 21, 7, 8, 5, 34, 4, 6]
>>> x.sort()
>>> x
[4, 5, 6, 7, 8, 21, 23, 34, 50, 74, 90]
>>> x.sort(reverse=True)
>>> x
[90, 74, 50, 34, 23, 21, 8, 7, 6, 5, 4]
>>> y = x
>>> z = y
>>> x
[90, 74, 50, 34, 23, 21, 8, 7, 6, 5, 4]
>>> y
[90, 74, 50, 34, 23, 21, 8, 7, 6, 5, 4]
>>> z
[90, 74, 50, 34, 23, 21, 8, 7, 6, 5, 4]
>>> x is y
True
>>> y is z
True
>>> x is z
True
>>> x
[90, 74, 50, 34, 23, 21, 8, 7, 6, 5, 4]
>>> x[:]
[90, 74, 50, 34, 23, 21, 8, 7, 6, 5, 4]
>>> y = x[:]
>>> x is y
False
>>> x == y
True
>>> y[0] = 100
>>> y
[100, 74, 50, 34, 23, 21, 8, 7, 6, 5, 4]
>>> x
[90, 74, 50, 34, 23, 21, 8, 7, 6, 5, 4]
>>> x.append([4,5,4,3,5,6,1])
>>> x
[90, 74, 50, 34, 23, 21, 8, 7, 6, 5, 4, [4, 5, 4, 3, 5, 6, 1]]
>>> y = x[:]
>>> x == y
True
>>> x is y
False
>>> x[0] = 100
>>> y
[90, 74, 50, 34, 23, 21, 8, 7, 6, 5, 4, [4, 5, 4, 3, 5, 6, 1]]
>>> x
[100, 74, 50, 34, 23, 21, 8, 7, 6, 5, 4, [4, 5, 4, 3, 5, 6, 1]]
>>> x[-1][0] = 400
>>> x
[100, 74, 50, 34, 23, 21, 8, 7, 6, 5, 4, [400, 5, 4, 3, 5, 6, 1]]
>>> y
[90, 74, 50, 34, 23, 21, 8, 7, 6, 5, 4, [400, 5, 4, 3, 5, 6, 1]]
>>> x[-1] is y[-1]
True
>>> import copy
>>> z = copy.deepcopy(x)
>>> z[-1] is x[-1]
False
>>> x
[100, 74, 50, 34, 23, 21, 8, 7, 6, 5, 4, [400, 5, 4, 3, 5, 6, 1]]
>>> y
[90, 74, 50, 34, 23, 21, 8, 7, 6, 5, 4, [400, 5, 4, 3, 5, 6, 1]]
>>> z
[100, 74, 50, 34, 23, 21, 8, 7, 6, 5, 4, [400, 5, 4, 3, 5, 6, 1]]
>>> z[-1][0] = 4
>>> z
[100, 74, 50, 34, 23, 21, 8, 7, 6, 5, 4, [4, 5, 4, 3, 5, 6, 1]]
>>> x
[100, 74, 50, 34, 23, 21, 8, 7, 6, 5, 4, [400, 5, 4, 3, 5, 6, 1]]
>>> y
[90, 74, 50, 34, 23, 21, 8, 7, 6, 5, 4, [400, 5, 4, 3, 5, 6, 1]]
>>> data = [['ram','shyam','tom','jerry'],['tcs','infy','wipro','ibm'],['it','hr','sales','it']]
>>> data[0]
['ram', 'shyam', 'tom', 'jerry']
>>> data[0][0]
'ram'
>>> data[1][0]
'tcs'
>>> data[2][0]
'it'
>>> data[1][0]
'tcs'
>>> data[0][1]
'shyam'
>>> data[1][1]
'infy'
>>> data[2][1]
'hr'
>>> for i in range(len(data)):
	print(data[0][i], data[1][i], data[2][i])

	
ram tcs it
shyam infy hr
tom wipro sales
>>> for i in range(len(data[0])):
	print(data[0][i], data[1][i], data[2][i])

	
ram tcs it
shyam infy hr
tom wipro sales
jerry ibm it
>>> data
[['ram', 'shyam', 'tom', 'jerry'], ['tcs', 'infy', 'wipro', 'ibm'], ['it', 'hr', 'sales', 'it']]
>>> for i in range(len(data)):
	for j in range(len(data[0]))
	print(data[j][i], data[j][i], data[j][i])
	
SyntaxError: invalid syntax
>>> 
>>> for i in range(len(data)):
	for j in range(len(data[0])):print(data[j][i], data[j][i], data[j][i])

	
ram ram ram
tcs tcs tcs
it it it
Traceback (most recent call last):
  File "<pyshell#122>", line 2, in <module>
    for j in range(len(data[0])):print(data[j][i], data[j][i], data[j][i])
IndexError: list index out of range
>>> for i in range(len(data)):
	for j in range(len(data[i])):
		print(data[j][i])

		
ram
tcs
it
Traceback (most recent call last):
  File "<pyshell#126>", line 3, in <module>
    print(data[j][i])
IndexError: list index out of range
>>> for i in range(len(data)):
	for j in range(len(data[i])):
		print(data[i][j])

		
ram
shyam
tom
jerry
tcs
infy
wipro
ibm
it
hr
sales
it
>>> for i in range(len(data)):
	for j in range(len(data[i])):
		print(data[j][i])

		
ram
tcs
it
Traceback (most recent call last):
  File "<pyshell#130>", line 3, in <module>
    print(data[j][i])
IndexError: list index out of range
>>> data
[['ram', 'shyam', 'tom', 'jerry'], ['tcs', 'infy', 'wipro', 'ibm'], ['it', 'hr', 'sales', 'it']]
>>> for i in range(len(data[0])):
	for j in range(len(data)):
		print(data[j][i])

		
ram
tcs
it
shyam
infy
hr
tom
wipro
sales
jerry
ibm
it
>>> for i in range(len(data[0])):
	for j in range(len(data)):
		print(data[j][i], end='')
	print()

	
ramtcsit
shyaminfyhr
tomwiprosales
jerryibmit
>>> for i in range(len(data[0])):
	for j in range(len(data)):
		print(data[j][i], end=',')
	print()

	
ram,tcs,it,
shyam,infy,hr,
tom,wipro,sales,
jerry,ibm,it,
>>> for i in range(len(data[0])):
	print(data[0][i], data[1][i], data[2][i])

	
ram tcs it
shyam infy hr
tom wipro sales
jerry ibm it
>>> data
[['ram', 'shyam', 'tom', 'jerry'], ['tcs', 'infy', 'wipro', 'ibm'], ['it', 'hr', 'sales', 'it']]
>>> 
