# to print prime number
a = int(input("enter a number"))
ans = "is prime"
for i in range(2, a):
    if a % i == 0:
        ans = "not prime"
        break
print(ans)



