number = int(input("Enter the number of terms:"))
n1, n2 = 0, 1
count = 0
# check if number of terms is valid
if number <= 0:
    print("Please enter a positive number")
# if there is only one term return n1
elif number == 1:
    print("Fibonacci series up to", number, ":")
    print(n1)
# generate Fibonacci sequence
else:
    print("Fibonacci sequence:")
    while count < number:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
