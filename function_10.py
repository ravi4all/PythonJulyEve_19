# def even(n):
#     return n % 2 == 0

# e = even(6)
# print(e)
numbers = [i for i in range(1,51)]
# e = []
# for i in range(len(numbers)):
#     # e.append(even(numbers[i]))
#     if even(numbers[i]):
#         e.append(numbers[i])
# print(e)

e = list(filter(lambda n : n % 2 == 0, numbers))
print(e)