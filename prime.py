#a=int(input("Enter a number:"))
#for i in range (2,a):
 #   if a%i==0:
  #      print("It is not prime number")
   #     break
#else:
 #   print("It is prime number")

    #To display prime number in certain range
#for n in range(2,21):
 #   ans=True
  #  for i in range(2,n):
   #     if n%i==0:
    #        ans=False
     #       break

    #if ans==True:
     #   print(n,"is prime")
    #else:
     #   print(n,"is not prime")

    #Find the prime number of certain range and put them in a list:
primes=[] #empty list
n=int(input("Enter the range"))
for n in range(2,n):
    ans=True
    for i in range(2,n):
        if n%i==0:
            ans=False
            break
    if ans==True:
        primes.append(n) #add to list if prime
print(primes)
