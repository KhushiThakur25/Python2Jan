file = open('data.txt','r')
#data = file.read()
#data = file.read(20)
#file.seek(28)
#data = file.read()
data = file.readlines()
print(data)
file.close()