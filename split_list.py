
a = [11,12,13,14,15,16,17,18,19,20,21]
b = []
c = []
mid = len(a)//2
for i in range(len(a)):
    if i <= mid :
        b.append(a[i])
    else:
        c.append(a[i])
print(b)
print(c)