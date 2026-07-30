num = int(input("Enter a number: "))
factorial=1
#check ifthe number is negative, positive or zero
if num<0:
    print("Factorial does not exists for negative numbers")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial= factorial * i
    print("The Factorial of",num, "is", factorial)
