# Dynamic Arguments
# *args
#
# def add(*x):
#     # print(x)
#     count = 0
#     for i in range(len(x)):
#         count += x[i]
#     print(count)
#
# add(2,3)
# add(5,6,4,5,7)
# add(6,8,4,6,8,5,3,4)

def emp(id,name,dept,*prev_companies):
    print("Id : {}".format(id))
    print("Name : {}".format(name))
    print("Dept : {}".format(dept))
    print("Companies : {}".format(prev_companies))

emp(101,'Raman','IT','HCL')
emp(102,'Shyam','HR','HCL','TCS')
emp(102,'Suresh','HR','INFY','IBM','TCS')