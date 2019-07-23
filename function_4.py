# Return Statement
'''
def add(x,y):
    z = x + y
    return z

def calc(a):
    print("Sum is",a)

a = add(4,5)
calc(a)
'''

def calc(x,y):
    z1 = x + y
    z2 = x - y
    z3 = x / y
    z4 = x * y
    return z1,z2,z3,z4

'''
output = calc(4,8)
print(output)
'''
a,b,c,d = calc(4,8)
print(a,b,c,d)


