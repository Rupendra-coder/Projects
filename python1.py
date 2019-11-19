#to check whether the input number is prime or not
n=0
a=int(input('Enter a no.:'))
for i in range(1,a+1):
    if (a%i)==0:
        n=n+1
if n<=2:
    print('Prime')
else:
    print('Not prime')