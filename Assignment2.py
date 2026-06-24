# Basic Calculator

num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
print("Select operation \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n " \
"5.Modulo \n 6.Exponentiation \n 7.Floor Division")
opnum=int(input("Enter your choice (1 - 7) : "))
if opnum==1:
    print("Addition : ",num1+num2)
elif opnum==2:
    print("Subtraction : ",num1-num2)
elif opnum==3:
    print("Multiplication : ",num1*num2)
elif opnum==4:
    if num2 != 0:
        print("Division : ",num1/num2)
    else:
        print("Division by Zero is not possible.")
elif opnum==5:
    print("Modulo : ",num1%num1)
elif opnum==6:
    print("Exponentiation : ",num1**num2)
elif opnum==7:
    print("Floor Division : ",num1//num2)
else:
    print("Invalid choice")


print("\t")


# Pattern

n=int(input("Enter number of rows : "))
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()