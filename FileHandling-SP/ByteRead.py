file = open('img.png','rb')
data = file.read()

file.close()

file = open('img_2.png','wb')
file.write(data)
file.close()