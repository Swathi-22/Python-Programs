
digits = input("Enter 3 Numbers :")
dig_split = list(map(int, digits.split()))
count = 0
for i in range(len(dig_split)):
    l = dig_split[0]
    r = dig_split[1]
    k = dig_split[2]
for j in range(l, r+1):
    if j % k == 0:
        count += 1

print("Count =",count)