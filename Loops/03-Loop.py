#Nested Loop
'''
for i in range(5):
    for j in range(5):
        for k in range(5):
            print(i,j,k)
'''
'''
*
**
***
****
*****
'''

for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print()

for i in range(10):
    for j in range(10 - i):
        print(" ", end='')
    for k in range(2*i + 1):
        print('*', end='')
    print()












