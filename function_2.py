a = 11

def add():
    global a
    a = 12
    b = 33
    c = a + b
    print(c)

add()
print("Value of a is",a)
