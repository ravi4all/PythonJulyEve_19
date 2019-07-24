def calc():
    x = 5
    y = 3

    def add():
        z = x + y
        return z

    def sub():
        z = x - y
        return z

    return add, sub

x = calc()
# print(x())
print(x[0]())