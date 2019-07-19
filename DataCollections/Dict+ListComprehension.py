Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 5,4,4,5,6,8,8,9
>>> x
(5, 4, 4, 5, 6, 8, 8, 9)
>>> x[0]
5
>>> x[-1]
9
>>> x[:5]
(5, 4, 4, 5, 6)
>>> x[0] = 100
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> emp = name, sal, dept = "Ramesh", 35000, "IT"
>>> emp
('Ramesh', 35000, 'IT')
>>> name
'Ramesh'
>>> sal
35000
>>> dept
'IT'
>>> name
'Ramesh'
>>> emp
('Ramesh', 35000, 'IT')
>>> 
>>> 
>>> 


>>> 
>>> 


>>> 

>>> 

>>> 

>>> 
>>> d = {"name":"Ram","age":35,"sal":45000,"dept":"IT"}
>>> d.keys()
dict_keys(['name', 'age', 'sal', 'dept'])
>>> d.values()
dict_values(['Ram', 35, 45000, 'IT'])
>>> d.items()
dict_items([('name', 'Ram'), ('age', 35), ('sal', 45000), ('dept', 'IT')])
>>> d["branch"] = "TCS"
>>> d
{'name': 'Ram', 'age': 35, 'sal': 45000, 'dept': 'IT', 'branch': 'TCS'}
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    d[0]
KeyError: 0
>>> d["name"]
'Ram'
>>> for data in d:
	print(data)

	
name
age
sal
dept
branch
>>> for data in d.values():
	print(data)

	
Ram
35
45000
IT
TCS
>>> for data in d.items():
	print(data)

	
('name', 'Ram')
('age', 35)
('sal', 45000)
('dept', 'IT')
('branch', 'TCS')
>>> for data in d.items():
	print("{} is {}".format(data[0],data[1]))

	
name is Ram
age is 35
sal is 45000
dept is IT
branch is TCS
>>> emp = {"names":["raman","suman","naman","kapil","kamal"],"dept":["IT","IT","HR","SALES","MARKETING"],"sal":[25000,34000,32000,40000,28000]}
>>> emp
{'names': ['raman', 'suman', 'naman', 'kapil', 'kamal'], 'dept': ['IT', 'IT', 'HR', 'SALES', 'MARKETING'], 'sal': [25000, 34000, 32000, 40000, 28000]}
>>> import pandas as pd
>>> pd.DataFrame(emp)
   names       dept    sal
0  raman         IT  25000
1  suman         IT  34000
2  naman         HR  32000
3  kapil      SALES  40000
4  kamal  MARKETING  28000
>>> emp["sales"]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    emp["sales"]
KeyError: 'sales'
>>> emp["nmaes"]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    emp["nmaes"]
KeyError: 'nmaes'
>>> emp["names"]
['raman', 'suman', 'naman', 'kapil', 'kamal']
>>> emp["names"][0]
'raman'
>>> emp["sal"][0]
25000
>>> emp["sal"][1]
34000
>>> emp["sal"][1] > 30000
True
>>> emp["sal"][2] > 30000
True
>>> emp["sal"][3] > 30000
True
>>> emp["sal"][4] > 30000
False
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/July/PythonEveRegular/DataCollections/Dictionary_1.py 
suman IT 34000
naman HR 32000
kapil SALES 40000
>>> df = pd.DataFrame(emp)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    df = pd.DataFrame(emp)
NameError: name 'pd' is not defined
>>> import pandas as pd
>>> df = pd.DataFrame(emp)
>>> df
   names       dept    sal
0  raman         IT  25000
1  suman         IT  34000
2  naman         HR  32000
3  kapil      SALES  40000
4  kamal  MARKETING  28000
>>> import matplotlib.pyplot as plt
>>> plt.bar(df["names"], df["sal"])
<BarContainer object of 5 artists>
>>> plt.show()
>>> votes = [355,118,45,32]
>>> names = ["BJP","CONG","SP+BSP","OTHERS"]
>>> plt.bar(names,votes)
<BarContainer object of 4 artists>
>>> plt.show()
>>> plt.pie(votes,labels=names)
([<matplotlib.patches.Wedge object at 0x000001DBF8C535C0>, <matplotlib.patches.Wedge object at 0x000001DBF8C53F98>, <matplotlib.patches.Wedge object at 0x000001DBF8C674E0>, <matplotlib.patches.Wedge object at 0x000001DBF8C679E8>], [Text(-0.48534315087277924, 0.987138301303765, 'BJP'), Text(0.018848512486278106, -1.0998385034072298, 'CONG'), Text(0.8935972502754805, -0.6414701507475623, 'SP+BSP'), Text(1.0816756704383257, -0.19994435221280676, 'OTHERS')])
>>> plt.show()
>>> plt.pie(votes,labels=names,startangle=90)
([<matplotlib.patches.Wedge object at 0x000001DBF8C4D8D0>, <matplotlib.patches.Wedge object at 0x000001DBF8C4DE10>, <matplotlib.patches.Wedge object at 0x000001DBF8B8E320>, <matplotlib.patches.Wedge object at 0x000001DBF8B8E7F0>], [Text(-0.987138301303765, -0.4853431508727792, 'BJP'), Text(1.0998385034072298, 0.01884851248627804, 'CONG'), Text(0.6414701507475623, 0.8935972502754805, 'SP+BSP'), Text(0.19994435221280682, 1.0816756704383257, 'OTHERS')])
>>> plt.show()
>>> plt.pie(votes,labels=names,startangle=90,counterclock=False)
([<matplotlib.patches.Wedge object at 0x000001DBF8BC0E48>, <matplotlib.patches.Wedge object at 0x000001DBF8BCC390>, <matplotlib.patches.Wedge object at 0x000001DBF8BCC860>, <matplotlib.patches.Wedge object at 0x000001DBF8BCCD30>], [Text(0.987138301303765, -0.4853431508727792, 'BJP'), Text(-1.0998385034072296, 0.018848512486278664, 'CONG'), Text(-0.6414701507475622, 0.8935972502754806, 'SP+BSP'), Text(-0.1999443522128067, 1.0816756704383257, 'OTHERS')])
>>> plt.show()
>>> plt.pie(votes,labels=names,startangle=90,counterclock=False,autopct='%1.2f%%')
([<matplotlib.patches.Wedge object at 0x000001DBF9BE9438>, <matplotlib.patches.Wedge object at 0x000001DBF9BE9B70>, <matplotlib.patches.Wedge object at 0x000001DBF9BF22B0>, <matplotlib.patches.Wedge object at 0x000001DBF9BF29B0>], [Text(0.987138301303765, -0.4853431508727792, 'BJP'), Text(-1.0998385034072296, 0.018848512486278664, 'CONG'), Text(-0.6414701507475622, 0.8935972502754806, 'SP+BSP'), Text(-0.1999443522128067, 1.0816756704383257, 'OTHERS')], [Text(0.5384390734384172, -0.2647326277487886, '64.55%'), Text(-0.5999119109493979, 0.010281006810697452, '21.45%'), Text(-0.34989280949867024, 0.48741668196844395, '8.18%'), Text(-0.10906055575244002, 0.5900049111481775, '5.82%')])
>>> plt.show()
>>> plt.pie(votes,labels=names,startangle=90,counterclock=False,autopct='%1.2f%%',explode=(0,0,0.2,0))
([<matplotlib.patches.Wedge object at 0x000001DBF9AC2358>, <matplotlib.patches.Wedge object at 0x000001DBF9AC2A90>, <matplotlib.patches.Wedge object at 0x000001DBF9ACB1D0>, <matplotlib.patches.Wedge object at 0x000001DBF9ACB8D0>], [Text(0.987138301303765, -0.4853431508727792, 'BJP'), Text(-1.0998385034072296, 0.018848512486278664, 'CONG'), Text(-0.758101087247119, 1.0560694775982953, 'SP+BSP'), Text(-0.1999443522128067, 1.0816756704383257, 'OTHERS')], [Text(0.5384390734384172, -0.2647326277487886, '64.55%'), Text(-0.5999119109493979, 0.010281006810697452, '21.45%'), Text(-0.466523745998227, 0.6498889092912586, '8.18%'), Text(-0.10906055575244002, 0.5900049111481775, '5.82%')])
>>> plt.show()
>>> plt.pie(votes,labels=names,startangle=90,counterclock=False,autopct='%1.2f%%',explode=(0,0,0.2,0),shadow=True)
([<matplotlib.patches.Wedge object at 0x000001DBF9B091D0>, <matplotlib.patches.Wedge object at 0x000001DBF9B09BA8>, <matplotlib.patches.Wedge object at 0x000001DBF9B12588>, <matplotlib.patches.Wedge object at 0x000001DBF9B12F28>], [Text(0.987138301303765, -0.4853431508727792, 'BJP'), Text(-1.0998385034072296, 0.018848512486278664, 'CONG'), Text(-0.758101087247119, 1.0560694775982953, 'SP+BSP'), Text(-0.1999443522128067, 1.0816756704383257, 'OTHERS')], [Text(0.5384390734384172, -0.2647326277487886, '64.55%'), Text(-0.5999119109493979, 0.010281006810697452, '21.45%'), Text(-0.466523745998227, 0.6498889092912586, '8.18%'), Text(-0.10906055575244002, 0.5900049111481775, '5.82%')])
>>> plt.show()
>>> plt.pie(votes,labels=names,startangle=90,counterclock=False,autopct='%1.2f%%',explode=(0,0,0.2,0),shadow=True)
([<matplotlib.patches.Wedge object at 0x000001DBF9B52898>, <matplotlib.patches.Wedge object at 0x000001DBF9B5E2B0>, <matplotlib.patches.Wedge object at 0x000001DBF9B5EC50>, <matplotlib.patches.Wedge object at 0x000001DBF9B66630>], [Text(0.987138301303765, -0.4853431508727792, 'BJP'), Text(-1.0998385034072296, 0.018848512486278664, 'CONG'), Text(-0.758101087247119, 1.0560694775982953, 'SP+BSP'), Text(-0.1999443522128067, 1.0816756704383257, 'OTHERS')], [Text(0.5384390734384172, -0.2647326277487886, '64.55%'), Text(-0.5999119109493979, 0.010281006810697452, '21.45%'), Text(-0.466523745998227, 0.6498889092912586, '8.18%'), Text(-0.10906055575244002, 0.5900049111481775, '5.82%')])
>>> plt.legend()
<matplotlib.legend.Legend object at 0x000001DBF8CA9EF0>
>>> plt.show()
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/July/PythonEveRegular/DataCollections/Dictionary_1.py 
>>> products
[{'p_id': 101, 'p_name': 'Apple Iphone XS', 'p_price': 90000}, {'p_id': 102, 'p_name': 'Apple Iphone XS Max', 'p_price': 120000}, {'p_id': 103, 'p_name': 'Samsung Galaxy S5', 'p_price': 76000}, {'p_id': 104, 'p_name': 'Redmi Note 6', 'p_price': 17000}, {'p_id': 105, 'p_name': 'Redmi Note 7', 'p_price': 22000}]
>>> products[0]
{'p_id': 101, 'p_name': 'Apple Iphone XS', 'p_price': 90000}
>>> products[0]["p_price"]
90000
>>> products[0]["p_price"] < 25000
False
>>> products[1]["p_price"] < 25000
False
>>> products[2]["p_price"] < 25000
False
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/July/PythonEveRegular/DataCollections/Dictionary_1.py 
{'p_id': 104, 'p_name': 'Redmi Note 6', 'p_price': 17000}
{'p_id': 105, 'p_name': 'Redmi Note 7', 'p_price': 22000}
>>> x = []
>>> for i in range(50):
	if i % 2 == 0:
		x.append(i)

		
>>> x
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> x = [i for i in range(50)]
>>> 
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> x = [i for i in range(50) if i % 2 == 0]
>>> x
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> x = [(i,j) for i in range(5) for j in range(5) if i != j]
>>> x
[(0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3)]
>>> x = [(i,j) for i in range(5) for j in range(5) for k in range(5) if i != j != k]
>>> x
[(0, 1), (0, 1), (0, 1), (0, 1), (0, 2), (0, 2), (0, 2), (0, 2), (0, 3), (0, 3), (0, 3), (0, 3), (0, 4), (0, 4), (0, 4), (0, 4), (1, 0), (1, 0), (1, 0), (1, 0), (1, 2), (1, 2), (1, 2), (1, 2), (1, 3), (1, 3), (1, 3), (1, 3), (1, 4), (1, 4), (1, 4), (1, 4), (2, 0), (2, 0), (2, 0), (2, 0), (2, 1), (2, 1), (2, 1), (2, 1), (2, 3), (2, 3), (2, 3), (2, 3), (2, 4), (2, 4), (2, 4), (2, 4), (3, 0), (3, 0), (3, 0), (3, 0), (3, 1), (3, 1), (3, 1), (3, 1), (3, 2), (3, 2), (3, 2), (3, 2), (3, 4), (3, 4), (3, 4), (3, 4), (4, 0), (4, 0), (4, 0), (4, 0), (4, 1), (4, 1), (4, 1), (4, 1), (4, 2), (4, 2), (4, 2), (4, 2), (4, 3), (4, 3), (4, 3), (4, 3)]
>>> x = [(i,j,k) for i in range(5) for j in range(5) for k in range(5) if i != j != k]
>>> x
[(0, 1, 0), (0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 0), (0, 2, 1), (0, 2, 3), (0, 2, 4), (0, 3, 0), (0, 3, 1), (0, 3, 2), (0, 3, 4), (0, 4, 0), (0, 4, 1), (0, 4, 2), (0, 4, 3), (1, 0, 1), (1, 0, 2), (1, 0, 3), (1, 0, 4), (1, 2, 0), (1, 2, 1), (1, 2, 3), (1, 2, 4), (1, 3, 0), (1, 3, 1), (1, 3, 2), (1, 3, 4), (1, 4, 0), (1, 4, 1), (1, 4, 2), (1, 4, 3), (2, 0, 1), (2, 0, 2), (2, 0, 3), (2, 0, 4), (2, 1, 0), (2, 1, 2), (2, 1, 3), (2, 1, 4), (2, 3, 0), (2, 3, 1), (2, 3, 2), (2, 3, 4), (2, 4, 0), (2, 4, 1), (2, 4, 2), (2, 4, 3), (3, 0, 1), (3, 0, 2), (3, 0, 3), (3, 0, 4), (3, 1, 0), (3, 1, 2), (3, 1, 3), (3, 1, 4), (3, 2, 0), (3, 2, 1), (3, 2, 3), (3, 2, 4), (3, 4, 0), (3, 4, 1), (3, 4, 2), (3, 4, 3), (4, 0, 1), (4, 0, 2), (4, 0, 3), (4, 0, 4), (4, 1, 0), (4, 1, 2), (4, 1, 3), (4, 1, 4), (4, 2, 0), (4, 2, 1), (4, 2, 3), (4, 2, 4), (4, 3, 0), (4, 3, 1), (4, 3, 2), (4, 3, 4)]
>>> d = {x : x**3 for x in range(10)}
>>> d
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}
>>> 
