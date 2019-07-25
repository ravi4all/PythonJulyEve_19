def temp_conv(c):
    return 9/5 * c + 32

# f = temp_conv(34.5)
# print(f)
temp = [34.5,43.2,44.5,40.6,39.8]
# temp_conv(temp)
# f = []
# for t in temp:
#     f.append(temp_conv(t))
#
# print(f)
f = list(map(temp_conv, temp))
print(f)

# def myMap(func, iter):
#     data = []
#     for i in iter:
#         data.append(func(i))
#     return data
#
# f = myMap(temp_conv, temp)
# print(f)