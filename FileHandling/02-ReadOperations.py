file = open('notes.txt')
# data = file.read()

# read data till 25th character
# data = file.read(25)

# start reading data from 25th character
# file.seek(25)
# data = file.read()

# read data line by line
# data = file.readline()

# read all the lines and return a list
data = file.readlines()
print(data)
file.close()