n = int(input("enter a number"))
ans = "It is prime"
for i in range(2, n):
   if n % i == 0:
       ans = "It is not prime"
       break
print(ans)
