minimum=int(input("Enter the minimum value:"))
maximum=int(input("Enter the highest value:"))
for number in range(minimum,maximum+1):
    if(number%2!=0):
        print("{0}".format(number))
