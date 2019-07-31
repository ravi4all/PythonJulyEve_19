file = open(r'C:\Users\asus\Documents\image_11.jpg','rb')
data = file.read()
file.close()

file = open('img_1.jpg','wb')
file.write(data)
file.close()