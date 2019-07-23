#Global Scope - accessible everywhere in program
a = 12
b = 22

# Function definition
def add():
    #Local Scope - limited to this function only
##    a = 12
##    b = 22
    c = a + b
    print(c)

def sub():
##    a = 12
##    b = 22
    c = a - b
    print(c)

# Function call
add()
sub()

z = a / b
z1 = a * b
print(z,z1)
