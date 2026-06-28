# find largest and smallest
a=[100,-6,683,2,234,4,-9,5,0,7]
largest = a[0]
smallest = a[0]

for i in a:
    if i > largest:
        largest = i
    
    if i < smallest:
        smallest = i

print("Largest element is " , largest)
print("Smallest element is ", smallest)