#to print list of prime numbers less than 21
primes= []
for n in range (2,21):
    ans= True
    for i in range(2,n):
        if n%i==0:
            ans= False
            break
    if ans==True:
        primes.append(n)
print(primes)
print(2%2)