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

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

ch = input("Enter your choice : ")
if ch == "1":
    x,y = takeInput()
    add(x,y)
elif ch == "2":
    x, y = takeInput()
    sub(x, y)
elif ch == "3":
    x, y = takeInput()
    mul(x, y)
elif ch == "4":
    x, y = takeInput()
    div(x, y)
else:
    print("Invalid Choice...")
