def add(x,y):
    z = x + y
    print("Sum is",z)

def sub(x,y):
    z = x - y
    print("Diff is",z)

def mul(x,y):
    z = x * y
    print("Mul is",z)

def div(x,y):
    z = x / y
    print("Div is",z)

def takeInput():
    f_num = int(input("Enter first number : "))
    s_num = int(input("Enter second number : "))
    return f_num, s_num

def errHandler(*args):
    print("Invalid Choice...")

print("""
1. Add
2. Sub
3. Mul
4. Div
""")

ch = input("Enter your choice : ")
x,y = takeInput()
# operations = [add(x,y),sub(x,y),mul(x,y),div(x,y)]
# operations[int(ch) - 1]

# First Method to build menu driven program
# operations = [add,sub,mul,div]
# operations[int(ch) - 1](x,y)

# Second Method
opr = {
    "1" : add,
    "2" : sub,
    "3" : mul,
    "4" : div
}
opr.get(ch,errHandler)(x,y)