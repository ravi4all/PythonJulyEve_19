def calc(x,y,opr):
    expression = x + opr + y
    result = eval(expression)
    print("Result is",result)

def takeInput():
    f_num = input("Enter first number : ")
    s_num = input("Enter second number : ")
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

operations = {
    "1" : "+",
    "2" : "-",
    "3" : "*",
    "4" : "/"
}
opr = operations.get(ch)
calc(x,y,opr)