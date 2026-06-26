# print list with non duplicates value

a=[1,2,3,4,5,6,7,1,1,1,4,4,4,5,5,5,8,8,9,10]
b=[]

for i in a:
    if i not in b:
        b.append(i)
print(b)

