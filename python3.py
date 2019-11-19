#to print prime numbers less than 21
for n in range(2,21):
    ans=0
    for i in range(2,n):
        if n%i==0:
            ans+=1
            break
    if ans<1:
        print(n,' is prime')
    else:
        print(n,' is not prime')