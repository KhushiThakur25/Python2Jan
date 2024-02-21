def temp_convert(c):
    return 9/5*c + 32

def km_to_m(km):
    return km*1000

temp = [34.2,65.1,32.4,91.1,42.7]
kms = [122,322,546,854,214,741]

'''f = []
for t in temp:
    f.append(temp_convert(t))

print(f)
    
m = []
for km in temp:
    m.append(km_to_m(km))

print(m)'''

'''def my_map(func,iter):
    data = []
    for i in range(len(iter)):
        data.append(func(iter[i]))
    return data'''
print(list(map(temp_convert,temp)))
print(list(map(km_to_m,kms)))

