a = int(input("enter a number"))
b = int(input("enter second number"))
c = int(input("enter third number"))
if (a > b) and (a > c):
    temp = a
elif (b > a) and (b > c):
    temp = b
else:
    temp = c
    print("The greatest number is ", temp)
